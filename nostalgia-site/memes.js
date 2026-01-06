// 2011 Memes, Portland Occupy Timeline, and Cultural References
// Narrative timeline from September - December 2011

// ============================================
// SEPT-DEC 2011 NARRATIVE TIMELINE (4 ACTS)
// ============================================
// Act 1: September - The Spark
// Act 2: October - The Surge  
// Act 3: November - The Crackdown
// Act 4: December - The Ports & Winter Break

const TIMELINE_2011 = [
    // === ACT 1: SEPTEMBER - THE SPARK ===
    {
        id: 1,
        date: '2011-09-17',
        month: 'september',
        act: 1,
        title: 'OCCUPY WALL STREET BEGINS',
        text: 'Protesters occupy Zuccotti Park in NYC',
        type: 'headline',
        location: 'NYC',
        mood: 'hope',
        source: 'Various news outlets'
    },
    {
        id: 2,
        date: '2011-09-23',
        month: 'september',
        act: 1,
        title: 'BITCOIN 0.4.0 RELEASED',
        text: 'First version with wallet encryption',
        type: 'headline',
        location: 'Internet',
        mood: 'tech',
        source: 'bitcoin.org'
    },
    {
        id: 3,
        date: '2011-09-24',
        month: 'september',
        act: 1,
        title: '"We are the 99%"',
        text: 'Tumblr launches, slogan spreads virally',
        type: 'quote',
        location: 'Internet',
        mood: 'hope',
        source: 'wearethe99percent.tumblr.com'
    },
    
    // === ACT 2: OCTOBER - THE SURGE ===
    {
        id: 4,
        date: '2011-10-06',
        month: 'october',
        act: 2,
        title: 'OCCUPY PORTLAND BEGINS',
        text: '4,000+ march through downtown - one of largest rallies in nation',
        type: 'headline',
        location: 'Portland',
        mood: 'energy',
        source: 'The Oregonian'
    },
    {
        id: 5,
        date: '2011-10-06',
        month: 'october',
        act: 2,
        title: '"This is what democracy looks like"',
        text: 'Chant echoes through Pioneer Courthouse Square',
        type: 'quote',
        location: 'Portland',
        mood: 'energy',
        source: 'Occupy Portland'
    },
    {
        id: 6,
        date: '2011-10-06',
        month: 'october',
        act: 2,
        title: '"Whose square? Our square!"',
        text: 'Protesters fill Pioneer Courthouse Square',
        type: 'quote',
        location: 'Portland',
        mood: 'energy',
        source: 'The Oregonian'
    },
    {
        id: 7,
        date: '2011-10-06',
        month: 'october',
        act: 2,
        title: 'Umbrella Man gets a sign',
        text: 'Portland icon holds "We are the 99%" sign',
        type: 'headline',
        location: 'Portland',
        mood: 'energy',
        source: 'The Oregonian'
    },
    {
        id: 8,
        date: '2011-10-09',
        month: 'october',
        act: 2,
        title: 'OCCUPY SPREADS TO 70+ CITIES',
        text: 'Movement goes nationwide',
        type: 'headline',
        location: 'USA',
        mood: 'momentum',
        source: 'Various'
    },
    {
        id: 9,
        date: '2011-10-15',
        month: 'october',
        act: 2,
        title: 'GLOBAL DAY OF ACTION',
        text: 'Protests in 900+ cities worldwide',
        type: 'headline',
        location: 'Global',
        mood: 'momentum',
        source: 'Various'
    },
    
    // === ACT 3: NOVEMBER - THE CRACKDOWN ===
    {
        id: 10,
        date: '2011-11-13',
        month: 'november',
        act: 3,
        title: 'POLICE EVICT OCCUPY PORTLAND',
        text: 'Riot police clear Lownsdale and Chapman Square parks',
        type: 'headline',
        location: 'Portland',
        mood: 'confrontation',
        source: 'BBC News'
    },
    {
        id: 11,
        date: '2011-11-13',
        month: 'november',
        act: 3,
        title: '"I don\'t see no riot here, take off your riot gear"',
        text: 'Protesters chant as police move in',
        type: 'quote',
        location: 'Portland',
        mood: 'confrontation',
        source: 'BBC News'
    },
    {
        id: 12,
        date: '2011-11-13',
        month: 'november',
        act: 3,
        title: '"The parks are gone, but the consciousness has not died"',
        text: 'Gina Ronning, Occupy Portland organizer',
        type: 'quote',
        location: 'Portland',
        mood: 'persistence',
        source: 'The Oregonian'
    },
    {
        id: 13,
        date: '2011-11-15',
        month: 'november',
        act: 3,
        title: 'NYPD RAIDS ZUCCOTTI PARK',
        text: 'Original Occupy camp cleared',
        type: 'headline',
        location: 'NYC',
        mood: 'confrontation',
        source: 'Various'
    },
    {
        id: 14,
        date: '2011-11-17',
        month: 'november',
        act: 3,
        title: 'NATIONAL DAY OF ACTION',
        text: '400 arrested nationwide, 300 in NYC',
        type: 'headline',
        location: 'USA',
        mood: 'confrontation',
        source: 'CBS News'
    },
    {
        id: 15,
        date: '2011-11-21',
        month: 'november',
        act: 3,
        title: 'BITCOIN 0.5.0 RELEASED',
        text: 'Improved wallet encryption',
        type: 'headline',
        location: 'Internet',
        mood: 'tech',
        source: 'bitcoin.org'
    },
    
    // === ACT 4: DECEMBER - THE PORTS & WINTER BREAK ===
    {
        id: 16,
        date: '2011-12-12',
        month: 'december',
        act: 4,
        title: 'OCCUPY THE PORTS',
        text: 'Portland protesters shut down Terminal 5 and 6',
        type: 'headline',
        location: 'Portland',
        mood: 'persistence',
        source: 'NPR'
    },
    {
        id: 17,
        date: '2011-12-12',
        month: 'december',
        act: 4,
        title: '"Shut Down Wall Street on the Waterfront"',
        text: 'West Coast port blockade coordinated action',
        type: 'quote',
        location: 'Portland',
        mood: 'persistence',
        source: 'Labor Notes'
    },
    {
        id: 18,
        date: '2011-12-12',
        month: 'december',
        act: 4,
        title: 'Protesters gather at Kelley Point Park',
        text: 'March to Marine Drive terminals',
        type: 'headline',
        location: 'Portland',
        mood: 'persistence',
        source: 'KING5'
    },
    {
        id: 19,
        date: '2011-12-17',
        month: 'december',
        act: 4,
        title: 'KIM JONG-IL DEAD AT 69',
        text: 'North Korean leader dies, world reacts',
        type: 'headline',
        location: 'World',
        mood: 'world',
        source: 'BBC News'
    },
    {
        id: 20,
        date: '2011-12-20',
        month: 'december',
        act: 4,
        title: 'CMU WINTER BREAK BEGINS',
        text: 'Students head home for the holidays',
        type: 'headline',
        location: 'Pittsburgh/Portland',
        mood: 'personal',
        source: 'CMU Academic Calendar'
    },
    {
        id: 21,
        date: '2011-12-25',
        month: 'december',
        act: 4,
        title: 'Christmas 2011',
        text: 'Family time, brother home from CMU...',
        type: 'headline',
        location: 'Portland',
        mood: 'personal',
        source: ''
    },
    {
        id: 22,
        date: '2012-01-01',
        month: 'january',
        act: 4,
        title: 'New Year 2012',
        text: 'Bitcoin wallet needs a password...',
        type: 'headline',
        location: 'Portland',
        mood: 'personal',
        source: ''
    }
];

// ============================================
// MEME IMAGES (2011 era authentic)
// ============================================
const MEME_SOURCES = [
    // === ANIMATED GIFS ===
    // Nyan Cat - THE 2011 meme (multiple versions)
    {
        url: 'https://media.giphy.com/media/sIIhZliB2McAo/giphy.gif',
        name: 'Nyan Cat',
        size: 120,
        isGif: true
    },
    {
        url: 'https://media.giphy.com/media/3o85xoi6nNqJQJ95Qc/giphy.gif',
        name: 'Nyan Cat Rainbow',
        size: 100,
        isGif: true
    },
    // Dancing Baby (classic internet)
    {
        url: 'https://media.giphy.com/media/l0MYyv6UK0Bd4DE76/giphy.gif',
        name: 'Dancing',
        size: 80,
        isGif: true
    },
    // Keyboard Cat
    {
        url: 'https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif',
        name: 'Keyboard Cat',
        size: 100,
        isGif: true
    },
    // Deal With It glasses
    {
        url: 'https://media.giphy.com/media/ENagATV1Gr9eg/giphy.gif',
        name: 'Deal With It',
        size: 80,
        isGif: true
    },
    // Dramatic Chipmunk
    {
        url: 'https://media.giphy.com/media/kKdgdeuO2M08M/giphy.gif',
        name: 'Dramatic Look',
        size: 90,
        isGif: true
    },
    // Rick Roll (classic)
    {
        url: 'https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif',
        name: 'Rick Roll',
        size: 100,
        isGif: true
    },
    // Trollface animated
    {
        url: 'https://media.giphy.com/media/amxLHEPgGDCKs/giphy.gif',
        name: 'Trollface Animated',
        size: 80,
        isGif: true
    },
    // Spinning rainbow
    {
        url: 'https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif',
        name: 'Rainbow Spin',
        size: 70,
        isGif: true
    },
    // Hacker typing
    {
        url: 'https://media.giphy.com/media/YQitE4YNQNahy/giphy.gif',
        name: 'Hacking',
        size: 100,
        isGif: true
    },
    // Matrix code
    {
        url: 'https://media.giphy.com/media/sULKEgDMX8LcI/giphy.gif',
        name: 'Matrix',
        size: 90,
        isGif: true
    },
    
    // === RAGE COMICS / MEME FACES ===
    // Trollface (static)
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/091/TrollFace.jpg',
        name: 'Trollface',
        size: 80
    },
    // Forever Alone
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/003/619/ForeverAlone.jpg',
        name: 'Forever Alone',
        size: 70
    },
    // Y U NO
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/004/006/y-u-no-guy.jpg',
        name: 'Y U NO',
        size: 80
    },
    // Me Gusta
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/002/252/NoMeGusta.jpg',
        name: 'Me Gusta',
        size: 70
    },
    // Rage Face / FFFUUU
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/063/Rage.jpg',
        name: 'FFFUUU',
        size: 70
    },
    // Okay Guy
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/003/617/OkayGuy.jpg',
        name: 'Okay',
        size: 70
    },
    // Challenge Accepted
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/004/457/challenge.jpg',
        name: 'Challenge Accepted',
        size: 70
    },
    // Cereal Guy
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/002/686/cereal_guy.jpg',
        name: 'Cereal Guy',
        size: 70
    },
    // Poker Face
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/003/193/1279052383758.jpg',
        name: 'Poker Face',
        size: 70
    },
    // LOL Face
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/281/lolface.jpg',
        name: 'LOL Face',
        size: 70
    },
    // Derp
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/006/423/ragecomic.png',
        name: 'Derp',
        size: 70
    },
    // Not Bad Obama
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/006/151/ObamaNotBad.jpg',
        name: 'Not Bad',
        size: 80
    },
    
    // === CLASSIC 2011 MEMES ===
    // Futurama Fry - Not Sure If
    {
        url: 'https://i.imgflip.com/1bgw.jpg',
        name: 'Not Sure If',
        size: 90
    },
    // Success Kid
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/745/success.jpg',
        name: 'Success Kid',
        size: 80
    },
    // Bad Luck Brian
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/006/707/nothing-to-do-here-template.jpg',
        name: 'Nothing To Do Here',
        size: 80
    },
    // Philosoraptor
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/046/Philosoraptor.jpg',
        name: 'Philosoraptor',
        size: 80
    },
    // Scumbag Steve
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/006/026/NOTSUREIF.jpg',
        name: 'Scumbag',
        size: 80
    },
    // Good Guy Greg
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/007/508/neildegrasse.jpg',
        name: 'Good Guy',
        size: 80
    },
    // Ancient Aliens Guy
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/005/848/Aliens.jpg',
        name: 'Aliens',
        size: 80
    },
    // One Does Not Simply
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/007/784/14-one-does-not-simply.jpg',
        name: 'One Does Not Simply',
        size: 90
    },
    // Doge (early version)
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg',
        name: 'Doge',
        size: 90
    },
    // All The Things
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/006/199/x-all-the-y.png',
        name: 'All The Things',
        size: 80
    },
    // Shut Up And Take My Money
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/005/574/takemymoney.jpg',
        name: 'Take My Money',
        size: 80
    },
    
    // === HACKER / TECH MEMES ===
    // Bitcoin logo (2011 era)
    {
        url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/200px-Bitcoin.svg.png',
        name: 'Bitcoin',
        size: 60
    },
    // Anonymous mask
    {
        url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Anonymous_emblem.svg/200px-Anonymous_emblem.svg.png',
        name: 'Anonymous',
        size: 70
    },
    // Hackerman
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/021/807/ig9OoyenpxqdCQyABmOQBZDI0duHk2QZZmWg2Hxd4ro.jpg',
        name: 'Hackerman',
        size: 90
    },
    
    // === POTATO / POOP (Dean references) ===
    // Potato
    {
        url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Patates.jpg/220px-Patates.jpg',
        name: 'Potato',
        size: 60
    },
    // Poop emoji (classic)
    {
        url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Twemoji_1f4a9.svg/200px-Twemoji_1f4a9.svg.png',
        name: 'Poop',
        size: 50
    },
    // I Can Has Cheezburger
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/774/lime-cat.jpg',
        name: 'Lime Cat',
        size: 80
    },
    // Ceiling Cat
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/016/ceilingcat.jpg',
        name: 'Ceiling Cat',
        size: 80
    },
    // Longcat
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/076/longcat.jpg',
        name: 'Longcat',
        size: 100
    },
    // Lolcat
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/026/lolcat.jpg',
        name: 'LOLcat',
        size: 80
    },
    // Pedobear (classic 4chan)
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/000/005/pedobear.jpg',
        name: 'Pedobear',
        size: 70
    },
    // This Is Fine
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/018/012/this_is_fine.jpeg',
        name: 'This Is Fine',
        size: 90
    },
    // Ermahgerd
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/009/479/Ermahgerd.jpg',
        name: 'Ermahgerd',
        size: 80
    },
    // Overly Attached Girlfriend
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/010/496/Overly_attached_GF.jpg',
        name: 'Overly Attached',
        size: 80
    },
    // Grumpy Cat
    {
        url: 'https://i.kym-cdn.com/entries/icons/original/000/014/285/sidecat.jpg',
        name: 'Grumpy Cat',
        size: 80
    }
];

// ============================================
// MUSIC - 2011 Hits + Hacker/Infosec Culture
// ============================================
// MIDI sources: bitmidi.com, freemidi.org, midiworld.com

const MUSIC_2011 = [
    // 2011 Pop Hits
    {
        title: 'Party Rock Anthem - LMFAO',
        youtubeId: 'KQ6zr6kCPj8',
        midiUrl: 'https://bitmidi.com/uploads/69296.mid',
        category: 'pop'
    },
    {
        title: 'Rolling in the Deep - Adele',
        youtubeId: 'rYEDA3JcQqw',
        category: 'pop'
    },
    {
        title: 'Moves Like Jagger - Maroon 5',
        youtubeId: 'iEPTlhBmwRg',
        category: 'pop'
    },
    {
        title: 'Nyan Cat',
        youtubeId: 'wZZ7oFKsKzY',
        category: 'meme'
    },
    {
        title: 'Angry Birds Theme - Ari Pulkkinen',
        youtubeId: '6DYJXSSgW08',
        category: 'game',
        note: 'Iconic 2011 mobile game theme'
    },
    
    // Hacker/Infosec Culture Music
    {
        title: 'Sandstorm - Darude',
        youtubeId: 'y6120QOlsfU',
        midiUrl: 'https://freemidi.org/download3-7791-sandstorm-darude',
        category: 'hacker',
        note: '1999 release but huge meme in early 2010s - "song name?" trolling'
    },
    {
        title: 'Hacker Music - ytcracker',
        youtubeId: 'NL0yFE0v6VI',
        category: 'nerdcore',
        note: 'DEF CON 19 performer, nerdcore pioneer'
    },
    {
        title: 'The Link - ytcracker',
        youtubeId: 'L41cCGnnjiw',
        category: 'nerdcore',
        note: 'Classic nerdcore track'
    },
    {
        title: 'Dual Core - All The Things',
        category: 'nerdcore',
        note: 'Nerdcore duo - "My Girlfriend\'s a Hacker"'
    },
    {
        title: 'MC Frontalot',
        category: 'nerdcore',
        note: 'Godfather of nerdcore hip-hop'
    },
    
    // Chiptune / 8-bit (DEF CON vibes)
    {
        title: 'Chiptune/8-bit music',
        category: 'chiptune',
        note: 'Game Boy, NES era sounds - popular at hacker cons'
    }
];

// MIDI file sources for the site
const MIDI_SOURCES = {
    partyRock: 'https://bitmidi.com/uploads/69296.mid',
    sandstorm: 'https://freemidi.org/getter-7791',
    // Note: For actual playback, use Web Audio API or Tone.js with MIDI.js
};

// December 2011 specific events for context
const DECEMBER_2011_EVENTS = [
    {
        date: 'December 17, 2011',
        event: 'Kim Jong-il dies',
        description: 'North Korean leader dies, major world news'
    },
    {
        date: 'November 21, 2011',
        event: 'Bitcoin 0.5.0 released',
        description: 'Latest Bitcoin version with improved wallet encryption'
    },
    {
        date: 'November 15, 2011',
        event: 'Occupy Wall Street evicted',
        description: 'NYPD raids Zuccotti Park, but movement continues'
    },
    {
        date: 'December 2011',
        event: 'CMU Winter Break',
        description: 'Students home for the holidays'
    }
];

// Energy drinks popular in 2011
const ENERGY_DRINKS_2011 = [
    'Monster Energy',
    'Red Bull',
    'NOS',
    'Rockstar',
    'Full Throttle',
    'AMP Energy',
    'Bawls'
];

// Common phrases Dean might use (based on research)
const DEAN_PHRASES = [
    'tables are hard',
    'spelling is hard',
    'datatypes are hard',
    'numbers are hard',
    'markdown is hard',
    'flask is hard',
    'typing is hard',
    'this is dumb',
    'this is stupid',
    'bad password',
    'very bad password',
    'this is a bad password',
    'this is a very bad password',
    'potato',
    'poop',
    'poopy',
    'pootato',
    'derp',
    'herp derp',
    'for the lulz'
];

// Export for use in app.js
window.TIMELINE_2011 = TIMELINE_2011;
window.MEME_SOURCES = MEME_SOURCES;
window.MUSIC_2011 = MUSIC_2011;
window.MIDI_SOURCES = MIDI_SOURCES;
window.DECEMBER_2011_EVENTS = DECEMBER_2011_EVENTS;
window.ENERGY_DRINKS_2011 = ENERGY_DRINKS_2011;
window.DEAN_PHRASES = DEAN_PHRASES;
