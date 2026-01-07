// 2011 Nostalgia Site - App Logic
// Floating timeline, A/B questions, password collection, music player

(function() {
    'use strict';

    // ============================================
    // API CONFIGURATION
    // ============================================
    // Backend API URL - deployed on fly.io
    const API_URL = window.NOSTALGIA_API_URL || 'https://app-alxmhaah.fly.dev';

    // ============================================
    // STATE MANAGEMENT
    // ============================================
    const state = {
        sessionId: localStorage.getItem('nostalgia_session_id') || null,
        abAnswers: JSON.parse(localStorage.getItem('nostalgia_ab_answers') || '{}'),
        passwordGuesses: [],
        currentView: 'main', // 'main', 'ab', 'guess', 'games'
        musicPlaying: false,
        currentTrackIndex: 0,
        floatingElements: [],
        timelineIndex: 0,
        currentABQuestion: parseInt(localStorage.getItem('nostalgia_ab_question') || '1'),
        totalABQuestions: 10
    };

    // ============================================
    // API FUNCTIONS
    // ============================================
    async function saveABAnswers() {
        try {
            const response = await fetch(`${API_URL}/api/ab-answers`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    session_id: state.sessionId,
                    answers: state.abAnswers
                })
            });
            const data = await response.json();
            if (data.session_id) {
                state.sessionId = data.session_id;
                localStorage.setItem('nostalgia_session_id', data.session_id);
            }
            console.log('A/B answers saved:', data);
            return data;
        } catch (error) {
            console.error('Failed to save A/B answers:', error);
            return null;
        }
    }

    async function savePasswordGuesses() {
        try {
            const response = await fetch(`${API_URL}/api/password-guesses`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    session_id: state.sessionId,
                    guesses: state.passwordGuesses
                })
            });
            const data = await response.json();
            if (data.session_id) {
                state.sessionId = data.session_id;
                localStorage.setItem('nostalgia_session_id', data.session_id);
            }
            console.log('Password guesses saved:', data);
            return data;
        } catch (error) {
            console.error('Failed to save password guesses:', error);
            return null;
        }
    }

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
        
        // Also spawn memes - more frequently!
        if (window.MEME_SOURCES && window.MEME_SOURCES.length > 0) {
            // Spawn several memes immediately at startup
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    const meme = window.MEME_SOURCES[Math.floor(Math.random() * window.MEME_SOURCES.length)];
                    if (meme && meme.url) {
                        createFloatingElement({ type: 'meme', ...meme });
                    }
                }, i * 500); // Stagger initial spawns
            }
            
            // Then spawn new memes every 2-4 seconds (much faster than before)
            setInterval(() => {
                const meme = window.MEME_SOURCES[Math.floor(Math.random() * window.MEME_SOURCES.length)];
                if (meme && meme.url) {
                    createFloatingElement({ type: 'meme', ...meme });
                }
            }, 2000 + Math.random() * 2000);
        }
    }

    // ============================================
    // A/B QUESTION HANDLING (One question at a time)
    // ============================================
    function initABQuestions() {
        const abOptions = document.querySelectorAll('.ab-option');
        
        // Show the current question and update progress
        showCurrentABQuestion();
        
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
                localStorage.setItem('nostalgia_ab_answers', JSON.stringify(state.abAnswers));
                
                // Visual feedback
                this.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    this.style.transform = '';
                }, 200);
                
                console.log('A/B Answers:', state.abAnswers);
                
                // Save to backend
                saveABAnswers();
                
                // Auto-advance to next question after a short delay
                setTimeout(() => {
                    advanceABQuestion();
                }, 500);
            });
        });
    }
    
    function showCurrentABQuestion() {
        const questions = document.querySelectorAll('.ab-question');
        const progress = document.getElementById('ab-progress');
        
        questions.forEach((q, index) => {
            const qNum = parseInt(q.dataset.question);
            if (qNum === state.currentABQuestion) {
                q.style.display = 'block';
                // Restore previous selection if any
                const prevAnswer = state.abAnswers[qNum];
                if (prevAnswer) {
                    q.querySelectorAll('.ab-option').forEach(opt => {
                        if (opt.dataset.value === prevAnswer) {
                            opt.classList.add('selected');
                        }
                    });
                }
            } else {
                q.style.display = 'none';
            }
        });
        
        if (progress) {
            progress.textContent = `Question ${state.currentABQuestion} of ${state.totalABQuestions}`;
        }
    }
    
    function advanceABQuestion() {
        // Move to next question (cycle back to 1 after 10)
        state.currentABQuestion = (state.currentABQuestion % state.totalABQuestions) + 1;
        localStorage.setItem('nostalgia_ab_question', state.currentABQuestion.toString());
        
        showCurrentABQuestion();
        
        // Close modal after completing all questions (optional - user can keep cycling)
        // For now, just show the next question
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
                
                // Save to backend
                savePasswordGuesses();
                
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
    // MUSIC PLAYER (Chiptune/8-bit audio - MIDI style)
    // Full controls: seek, next, previous, shuffle
    // ============================================
    let audioPlayer = null;
    let shuffleMode = false;
    let shuffledPlaylist = [];
    let shuffleIndex = 0;
    
    function initMusicPlayer() {
        const toggleBtn = document.getElementById('toggle-music');
        const nowPlaying = document.getElementById('now-playing');
        const btnPrev = document.getElementById('btn-prev');
        const btnNext = document.getElementById('btn-next');
        const btnShuffle = document.getElementById('btn-shuffle');
        const seekBar = document.getElementById('seek-bar');
        const currentTimeEl = document.getElementById('current-time');
        const durationEl = document.getElementById('duration');
        
        if (!toggleBtn) return;
        
        // Create audio element
        audioPlayer = new Audio();
        audioPlayer.loop = false;
        audioPlayer.volume = 0.5;
        
        // Update seek bar and time display as track plays
        audioPlayer.addEventListener('timeupdate', () => {
            if (audioPlayer.duration) {
                const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
                if (seekBar) seekBar.value = percent;
                if (currentTimeEl) currentTimeEl.textContent = formatTime(audioPlayer.currentTime);
            }
        });
        
        // Update duration when metadata loads
        audioPlayer.addEventListener('loadedmetadata', () => {
            if (durationEl) durationEl.textContent = formatTime(audioPlayer.duration);
            if (seekBar) seekBar.value = 0;
            if (currentTimeEl) currentTimeEl.textContent = '0:00';
        });
        
        // Auto-advance to next track when current ends
        audioPlayer.addEventListener('ended', () => {
            nextTrack();
        });
        
        // Seek bar interaction
        if (seekBar) {
            seekBar.addEventListener('input', () => {
                if (audioPlayer.duration) {
                    const seekTime = (seekBar.value / 100) * audioPlayer.duration;
                    audioPlayer.currentTime = seekTime;
                }
            });
        }
        
        // Play/Pause toggle
        toggleBtn.addEventListener('click', function() {
            if (state.musicPlaying) {
                pauseMusic();
                this.innerHTML = '&#9654;';
                this.classList.remove('playing');
            } else {
                playMusic();
                this.innerHTML = '&#9208;';
                this.classList.add('playing');
            }
            state.musicPlaying = !state.musicPlaying;
        });
        
        // Previous track
        if (btnPrev) {
            btnPrev.addEventListener('click', () => {
                prevTrack();
            });
        }
        
        // Next track
        if (btnNext) {
            btnNext.addEventListener('click', () => {
                nextTrack();
            });
        }
        
        // Shuffle toggle
        if (btnShuffle) {
            btnShuffle.addEventListener('click', () => {
                shuffleMode = !shuffleMode;
                btnShuffle.classList.toggle('active', shuffleMode);
                if (shuffleMode) {
                    generateShuffledPlaylist();
                }
            });
        }
    }
    
    function formatTime(seconds) {
        if (!seconds || isNaN(seconds)) return '0:00';
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }
    
    function generateShuffledPlaylist() {
        const tracksWithAudio = window.MUSIC_2011 ? window.MUSIC_2011.filter(t => t.audioUrl) : [];
        shuffledPlaylist = [...Array(tracksWithAudio.length).keys()];
        for (let i = shuffledPlaylist.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffledPlaylist[i], shuffledPlaylist[j]] = [shuffledPlaylist[j], shuffledPlaylist[i]];
        }
        shuffleIndex = 0;
    }
    
    function getNextTrackIndex() {
        const tracksWithAudio = window.MUSIC_2011 ? window.MUSIC_2011.filter(t => t.audioUrl) : [];
        if (tracksWithAudio.length === 0) return 0;
        
        if (shuffleMode) {
            shuffleIndex = (shuffleIndex + 1) % shuffledPlaylist.length;
            return shuffledPlaylist[shuffleIndex];
        } else {
            return (state.currentTrackIndex + 1) % tracksWithAudio.length;
        }
    }
    
    function getPrevTrackIndex() {
        const tracksWithAudio = window.MUSIC_2011 ? window.MUSIC_2011.filter(t => t.audioUrl) : [];
        if (tracksWithAudio.length === 0) return 0;
        
        if (shuffleMode) {
            shuffleIndex = (shuffleIndex - 1 + shuffledPlaylist.length) % shuffledPlaylist.length;
            return shuffledPlaylist[shuffleIndex];
        } else {
            return (state.currentTrackIndex - 1 + tracksWithAudio.length) % tracksWithAudio.length;
        }
    }
    
    function nextTrack() {
        state.currentTrackIndex = getNextTrackIndex();
        if (state.musicPlaying) {
            playMusic();
        }
    }
    
    function prevTrack() {
        if (audioPlayer && audioPlayer.currentTime > 3) {
            audioPlayer.currentTime = 0;
        } else {
            state.currentTrackIndex = getPrevTrackIndex();
            if (state.musicPlaying) {
                playMusic();
            }
        }
    }
    
    function playMusic() {
        if (!window.MUSIC_2011 || window.MUSIC_2011.length === 0) return;
        
        const tracksWithAudio = window.MUSIC_2011.filter(t => t.audioUrl);
        
        if (tracksWithAudio.length > 0) {
            const track = tracksWithAudio[state.currentTrackIndex % tracksWithAudio.length];
            
            if (audioPlayer) {
                if (audioPlayer.src !== track.audioUrl) {
                    audioPlayer.src = track.audioUrl;
                }
                audioPlayer.play().catch(e => {
                    console.log('Audio autoplay blocked, user interaction required:', e);
                });
            }
            
            const nowPlaying = document.getElementById('now-playing');
            if (nowPlaying) {
                nowPlaying.textContent = track.title;
            }
        } else {
            const tracksWithYT = window.MUSIC_2011.filter(t => t.youtubeId);
            if (tracksWithYT.length === 0) return;
            
            const track = tracksWithYT[state.currentTrackIndex % tracksWithYT.length];
            
            let youtubePlayer = document.getElementById('youtube-player');
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
    }
    
    function pauseMusic() {
        if (audioPlayer) {
            audioPlayer.pause();
        }
    }
    
    function stopMusic() {
        if (audioPlayer) {
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
        }
        
        const youtubePlayer = document.getElementById('youtube-player');
        if (youtubePlayer) {
            youtubePlayer.src = '';
        }
    }

    // ============================================
    // BOTTOM NAVIGATION & MODAL HANDLING
    // ============================================
    function initBottomNav() {
        // Add styles for floating elements (injected dynamically)
        const style = document.createElement('style');
        style.textContent = `
            #bottom-nav {
                position: fixed;
                bottom: 80px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 50;
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
        
        // Event listeners for bottom nav buttons
        document.getElementById('nav-ab').addEventListener('click', () => {
            openModal('ab-modal');
        });
        
        document.getElementById('nav-guess').addEventListener('click', () => {
            openModal('guess-modal');
        });
        
        document.getElementById('nav-games').addEventListener('click', () => {
            openModal('games-modal');
            // Load video when games modal opens
            const video = document.getElementById('game-video');
            if (video && !video.src) {
                video.src = 'https://www.youtube.com/embed/eSMeUPFjQHc?autoplay=1';
            }
        });
        
        // Setup modal close buttons
        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', function() {
                const modal = this.closest('.modal-overlay');
                closeModal(modal.id);
            });
        });
        
        // Close modal when clicking outside content
        document.querySelectorAll('.modal-overlay').forEach(modal => {
            modal.addEventListener('click', function(e) {
                if (e.target === this) {
                    closeModal(this.id);
                }
            });
        });
    }
    
    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('active');
        }
    }
    
    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');
            // Stop video when closing games modal
            if (modalId === 'games-modal') {
                const video = document.getElementById('game-video');
                if (video) {
                    video.src = '';
                }
            }
        }
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
