// 2011 Nostalgia Site - App Logic
// Floating timeline, A/B questions, password collection, music player

(function() {
    'use strict';

    // ============================================
    // STATE MANAGEMENT
    // ============================================
    const state = {
        abAnswers: {},
        passwordGuesses: [],
        currentView: 'main', // 'main', 'ab', 'guess', 'games'
        musicPlaying: false,
        currentTrackIndex: 0,
        floatingElements: [],
        timelineIndex: 0
    };

    // ============================================
    // FLOATING TIMELINE SYSTEM (bumble.0x88.net/v style)
    // ============================================
    const memeContainer = document.getElementById('meme-container');
    
    function createFloatingElement(item) {
        const el = document.createElement('div');
        el.className = 'floating-item';
        
        // Determine element type based on item
        if (item.type === 'headline') {
            el.innerHTML = `
                <div class="floating-headline ${item.mood || ''}">
                    <span class="headline-date">${formatDate(item.date)}</span>
                    <span class="headline-text">${item.title}</span>
                    ${item.text ? `<span class="headline-subtext">${item.text}</span>` : ''}
                </div>
            `;
        } else if (item.type === 'quote') {
            el.innerHTML = `
                <div class="floating-quote ${item.mood || ''}">
                    <span class="quote-text">"${item.text}"</span>
                    ${item.source ? `<span class="quote-source">- ${item.source}</span>` : ''}
                </div>
            `;
        } else if (item.type === 'meme' && item.url) {
            el.innerHTML = `<img src="${item.url}" alt="${item.title || 'meme'}" class="floating-meme-img">`;
        } else {
            el.innerHTML = `
                <div class="floating-event ${item.mood || ''}">
                    <span class="event-title">${item.title}</span>
                </div>
            `;
        }
        
        // Random starting position (from edges)
        const side = Math.floor(Math.random() * 4); // 0=top, 1=right, 2=bottom, 3=left
        let startX, startY, endX, endY;
        
        switch(side) {
            case 0: // from top
                startX = Math.random() * window.innerWidth;
                startY = -100;
                endX = Math.random() * window.innerWidth;
                endY = window.innerHeight + 100;
                break;
            case 1: // from right
                startX = window.innerWidth + 100;
                startY = Math.random() * window.innerHeight;
                endX = -300;
                endY = Math.random() * window.innerHeight;
                break;
            case 2: // from bottom
                startX = Math.random() * window.innerWidth;
                startY = window.innerHeight + 100;
                endX = Math.random() * window.innerWidth;
                endY = -100;
                break;
            case 3: // from left
                startX = -300;
                startY = Math.random() * window.innerHeight;
                endX = window.innerWidth + 100;
                endY = Math.random() * window.innerHeight;
                break;
        }
        
        el.style.left = startX + 'px';
        el.style.top = startY + 'px';
        el.style.opacity = '0';
        
        memeContainer.appendChild(el);
        
        // Animate across screen
        const duration = 15000 + Math.random() * 10000; // 15-25 seconds
        const startTime = Date.now();
        
        function animate() {
            const elapsed = Date.now() - startTime;
            const progress = elapsed / duration;
            
            if (progress >= 1) {
                el.remove();
                return;
            }
            
            const x = startX + (endX - startX) * progress;
            const y = startY + (endY - startY) * progress;
            const opacity = progress < 0.1 ? progress * 10 : (progress > 0.9 ? (1 - progress) * 10 : 1);
            
            el.style.left = x + 'px';
            el.style.top = y + 'px';
            el.style.opacity = opacity * 0.8;
            
            requestAnimationFrame(animate);
        }
        
        requestAnimationFrame(animate);
    }
    
    function formatDate(dateStr) {
        if (!dateStr) return '';
        const date = new Date(dateStr);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${months[date.getMonth()]} ${date.getDate()}`;
    }
    
    // Spawn timeline items progressively
    function startTimelineSpawner() {
        if (!window.TIMELINE_2011 || window.TIMELINE_2011.length === 0) {
            console.warn('No timeline data available');
            return;
        }
        
        let index = 0;
        
        function spawnNext() {
            if (index < window.TIMELINE_2011.length) {
                createFloatingElement(window.TIMELINE_2011[index]);
                index++;
            } else {
                // Loop back to start
                index = 0;
            }
            
            // Spawn every 3-6 seconds
            setTimeout(spawnNext, 3000 + Math.random() * 3000);
        }
        
        // Start spawning
        spawnNext();
        
        // Also spawn some memes
        if (window.MEME_SOURCES) {
            setInterval(() => {
                const meme = window.MEME_SOURCES[Math.floor(Math.random() * window.MEME_SOURCES.length)];
                if (meme && meme.url) {
                    createFloatingElement({ type: 'meme', ...meme });
                }
            }, 8000 + Math.random() * 4000);
        }
    }

    // ============================================
    // A/B QUESTION HANDLING
    // ============================================
    function initABQuestions() {
        const abOptions = document.querySelectorAll('.ab-option');
        
        abOptions.forEach(option => {
            option.addEventListener('click', function() {
                const question = this.closest('.ab-question');
                const questionNum = question.dataset.question;
                const value = this.dataset.value;
                
                // Deselect siblings
                question.querySelectorAll('.ab-option').forEach(opt => {
                    opt.classList.remove('selected');
                });
                
                // Select this one
                this.classList.add('selected');
                
                // Store answer
                state.abAnswers[questionNum] = value;
                
                // Visual feedback
                this.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    this.style.transform = '';
                }, 200);
                
                console.log('A/B Answers:', state.abAnswers);
            });
        });
    }

    // ============================================
    // PASSWORD GUESS COLLECTION
    // ============================================
    function initGuessCollection() {
        const submitBtn = document.getElementById('submit-guesses');
        
        if (submitBtn) {
            submitBtn.addEventListener('click', function() {
                const guesses = [];
                for (let i = 1; i <= 5; i++) {
                    const input = document.getElementById('guess' + i);
                    if (input && input.value.trim()) {
                        guesses.push(input.value.trim());
                    }
                }
                
                state.passwordGuesses = guesses;
                
                // Show results
                showResults();
            });
        }
    }
    
    function showResults() {
        const resultsSection = document.getElementById('results-section');
        const resultsContent = document.getElementById('results-content');
        
        if (!resultsSection || !resultsContent) return;
        
        // Build profile based on A/B answers
        let profile = 'PASSWORD PROFILE\n';
        profile += '================\n\n';
        
        profile += 'A/B Test Results:\n';
        for (const [q, a] of Object.entries(state.abAnswers)) {
            profile += `  Q${q}: ${a}\n`;
        }
        
        profile += '\nPassword Guesses:\n';
        state.passwordGuesses.forEach((guess, i) => {
            profile += `  ${i + 1}. ${guess}\n`;
        });
        
        profile += '\n================\n';
        profile += 'Generated: ' + new Date().toISOString();
        
        resultsContent.textContent = profile;
        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
        
        // Copy button
        const copyBtn = document.getElementById('copy-results');
        if (copyBtn) {
            copyBtn.addEventListener('click', function() {
                navigator.clipboard.writeText(profile).then(() => {
                    this.textContent = 'Copied!';
                    setTimeout(() => {
                        this.textContent = 'Copy Results';
                    }, 2000);
                });
            });
        }
    }

    // ============================================
    // MUSIC PLAYER (YouTube embeds)
    // ============================================
    let youtubePlayer = null;
    
    function initMusicPlayer() {
        const toggleBtn = document.getElementById('toggle-music');
        const nowPlaying = document.getElementById('now-playing');
        
        if (!toggleBtn) return;
        
        toggleBtn.addEventListener('click', function() {
            if (state.musicPlaying) {
                stopMusic();
                this.textContent = 'Play 2011 Music';
                this.classList.remove('playing');
                nowPlaying.textContent = '';
            } else {
                playMusic();
                this.textContent = 'Stop Music';
                this.classList.add('playing');
            }
            state.musicPlaying = !state.musicPlaying;
        });
    }
    
    function playMusic() {
        if (!window.MUSIC_2011 || window.MUSIC_2011.length === 0) return;
        
        // Find a track with a YouTube ID
        const tracksWithYT = window.MUSIC_2011.filter(t => t.youtubeId);
        if (tracksWithYT.length === 0) return;
        
        const track = tracksWithYT[state.currentTrackIndex % tracksWithYT.length];
        
        // Create hidden YouTube iframe for audio
        if (!youtubePlayer) {
            youtubePlayer = document.createElement('iframe');
            youtubePlayer.id = 'youtube-player';
            youtubePlayer.style.display = 'none';
            youtubePlayer.allow = 'autoplay';
            document.body.appendChild(youtubePlayer);
        }
        
        youtubePlayer.src = `https://www.youtube.com/embed/${track.youtubeId}?autoplay=1&loop=1`;
        
        const nowPlaying = document.getElementById('now-playing');
        if (nowPlaying) {
            nowPlaying.textContent = track.title;
        }
    }
    
    function stopMusic() {
        if (youtubePlayer) {
            youtubePlayer.src = '';
        }
    }

    // ============================================
    // BOTTOM NAVIGATION
    // ============================================
    function initBottomNav() {
        // Create bottom navigation bar
        const nav = document.createElement('div');
        nav.id = 'bottom-nav';
        nav.innerHTML = `
            <button id="nav-ab" class="nav-btn">A/B Test</button>
            <button id="nav-guess" class="nav-btn">Guess Password</button>
            <button id="nav-games" class="nav-btn">Play Games</button>
        `;
        document.body.appendChild(nav);
        
        // Add styles for bottom nav
        const style = document.createElement('style');
        style.textContent = `
            #bottom-nav {
                position: fixed;
                bottom: 80px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 100;
                display: flex;
                gap: 15px;
                background: rgba(0,0,0,0.8);
                padding: 15px 25px;
                border-radius: 40px;
                border: 2px solid rgba(255,255,255,0.2);
            }
            
            .nav-btn {
                padding: 12px 24px;
                background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
                border: none;
                border-radius: 25px;
                color: #fff;
                font-size: 0.95rem;
                cursor: pointer;
                transition: all 0.3s;
                font-family: 'Comic Neue', cursive;
            }
            
            .nav-btn:hover {
                transform: scale(1.05);
                box-shadow: 0 5px 20px rgba(52, 152, 219, 0.4);
            }
            
            #nav-ab {
                background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            }
            
            #nav-guess {
                background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
            }
            
            #nav-games {
                background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
            }
            
            /* Floating element styles */
            .floating-item {
                position: absolute;
                z-index: 5;
                pointer-events: none;
                max-width: 300px;
            }
            
            .floating-headline {
                background: rgba(0,0,0,0.8);
                padding: 12px 18px;
                border-radius: 8px;
                border-left: 4px solid #f39c12;
                font-family: 'Press Start 2P', cursive;
            }
            
            .floating-headline.hope { border-left-color: #2ecc71; }
            .floating-headline.tech { border-left-color: #3498db; }
            .floating-headline.energy { border-left-color: #f39c12; }
            .floating-headline.momentum { border-left-color: #e67e22; }
            .floating-headline.confrontation { border-left-color: #e74c3c; }
            .floating-headline.persistence { border-left-color: #9b59b6; }
            .floating-headline.personal { border-left-color: #1abc9c; }
            
            .headline-date {
                display: block;
                font-size: 0.6rem;
                color: #bdc3c7;
                margin-bottom: 5px;
            }
            
            .headline-text {
                display: block;
                font-size: 0.7rem;
                color: #fff;
                line-height: 1.4;
            }
            
            .headline-subtext {
                display: block;
                font-size: 0.55rem;
                color: #95a5a6;
                margin-top: 5px;
            }
            
            .floating-quote {
                background: rgba(155, 89, 182, 0.8);
                padding: 15px;
                border-radius: 10px;
                font-style: italic;
            }
            
            .quote-text {
                display: block;
                font-size: 0.9rem;
                color: #fff;
            }
            
            .quote-source {
                display: block;
                font-size: 0.7rem;
                color: #d5b8e8;
                margin-top: 8px;
                text-align: right;
            }
            
            .floating-event {
                background: rgba(52, 152, 219, 0.8);
                padding: 10px 15px;
                border-radius: 20px;
            }
            
            .event-title {
                font-size: 0.8rem;
                color: #fff;
            }
            
            .floating-meme-img {
                max-width: 150px;
                max-height: 150px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }
            
            /* Games modal */
            #games-modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.9);
                z-index: 1000;
                justify-content: center;
                align-items: center;
            }
            
            #games-modal.active {
                display: flex;
            }
            
            .games-content {
                background: #1a1a2e;
                padding: 40px;
                border-radius: 20px;
                max-width: 600px;
                text-align: center;
            }
            
            .games-content h2 {
                font-family: 'Press Start 2P', cursive;
                color: #f39c12;
                margin-bottom: 30px;
            }
            
            .game-links {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            
            .game-link {
                padding: 20px;
                background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
                border-radius: 15px;
                color: #fff;
                text-decoration: none;
                font-size: 1.1rem;
                transition: transform 0.3s;
            }
            
            .game-link:hover {
                transform: scale(1.05);
            }
            
            .close-modal {
                margin-top: 30px;
                padding: 10px 30px;
                background: #e74c3c;
                border: none;
                border-radius: 20px;
                color: #fff;
                cursor: pointer;
            }
            
            @media (max-width: 768px) {
                #bottom-nav {
                    flex-direction: column;
                    bottom: 70px;
                    padding: 10px 15px;
                }
                
                .nav-btn {
                    padding: 10px 20px;
                    font-size: 0.85rem;
                }
            }
        `;
        document.head.appendChild(style);
        
        // Event listeners
        document.getElementById('nav-ab').addEventListener('click', () => {
            document.getElementById('ab-section').scrollIntoView({ behavior: 'smooth' });
        });
        
        document.getElementById('nav-guess').addEventListener('click', () => {
            document.getElementById('guess-section').scrollIntoView({ behavior: 'smooth' });
        });
        
        document.getElementById('nav-games').addEventListener('click', () => {
            showGamesModal();
        });
    }
    
    function showGamesModal() {
        // Create modal if it doesn't exist
        let modal = document.getElementById('games-modal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'games-modal';
            modal.innerHTML = `
                <div class="games-content">
                    <h2>2011 Browser Games</h2>
                    <div class="game-links">
                        <a href="https://poki.com/en/g/qwop" target="_blank" class="game-link">
                            QWOP - The Impossible Running Game
                        </a>
                        <a href="https://poki.com/en/g/robot-unicorn-attack" target="_blank" class="game-link">
                            Robot Unicorn Attack - Always I Wanna Be With You
                        </a>
                    </div>
                    <button class="close-modal">Close</button>
                </div>
            `;
            document.body.appendChild(modal);
            
            modal.querySelector('.close-modal').addEventListener('click', () => {
                modal.classList.remove('active');
            });
            
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.remove('active');
                }
            });
        }
        
        modal.classList.add('active');
    }

    // ============================================
    // WALLET PROMPT INTERACTION
    // ============================================
    function initWalletPrompt() {
        const okBtn = document.getElementById('btn-ok');
        const cancelBtn = document.getElementById('btn-cancel');
        const passphrase1 = document.getElementById('passphrase1');
        const passphrase2 = document.getElementById('passphrase2');
        
        if (okBtn) {
            okBtn.addEventListener('click', () => {
                const p1 = passphrase1.value;
                const p2 = passphrase2.value;
                
                if (!p1) {
                    alert('Please enter a passphrase');
                    return;
                }
                
                if (p1 !== p2) {
                    alert('Passphrases do not match!');
                    return;
                }
                
                // Store as first guess
                const guess1 = document.getElementById('guess1');
                if (guess1 && !guess1.value) {
                    guess1.value = p1;
                }
                
                alert('Passphrase saved! Scroll down to complete the A/B test and add more guesses.');
                document.getElementById('ab-section').scrollIntoView({ behavior: 'smooth' });
            });
        }
        
        if (cancelBtn) {
            cancelBtn.addEventListener('click', () => {
                passphrase1.value = '';
                passphrase2.value = '';
            });
        }
    }

    // ============================================
    // NYAN CAT RAINBOW TRAIL (Easter egg)
    // ============================================
    function initNyanTrail() {
        let lastTrailTime = 0;
        
        document.addEventListener('mousemove', (e) => {
            const now = Date.now();
            if (now - lastTrailTime < 50) return;
            lastTrailTime = now;
            
            // Only create trail 10% of the time for subtlety
            if (Math.random() > 0.1) return;
            
            const trail = document.createElement('div');
            trail.className = 'nyan-trail';
            trail.style.left = e.clientX + 'px';
            trail.style.top = e.clientY + 'px';
            trail.style.width = (20 + Math.random() * 30) + 'px';
            document.body.appendChild(trail);
            
            setTimeout(() => trail.remove(), 2000);
        });
    }

    // ============================================
    // INITIALIZATION
    // ============================================
    function init() {
        console.log('2011 Nostalgia Site initializing...');
        
        // Wait for DOM and data
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAll);
        } else {
            initAll();
        }
    }
    
    function initAll() {
        initBottomNav();
        initABQuestions();
        initGuessCollection();
        initMusicPlayer();
        initWalletPrompt();
        initNyanTrail();
        
        // Start floating timeline after a short delay
        setTimeout(startTimelineSpawner, 1000);
        
        console.log('2011 Nostalgia Site ready!');
        console.log('Timeline items:', window.TIMELINE_2011 ? window.TIMELINE_2011.length : 0);
        console.log('Music tracks:', window.MUSIC_2011 ? window.MUSIC_2011.length : 0);
    }
    
    init();
})();
