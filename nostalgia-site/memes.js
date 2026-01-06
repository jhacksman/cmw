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
    // Nyan Cat - THE 2011 meme
    {
        url: 'https://media.giphy.com/media/sIIhZliB2McAo/giphy.gif',
        name: 'Nyan Cat',
        size: 100
    },
    // Trollface
    {
        url: 'https://upload.wikimedia.org/wikipedia/en/9/9a/Trollface_non-free.png',
        name: 'Trollface',
        size: 80
    },
    // Forever Alone
    {
        url: 'https://i.imgflip.com/1c1uej.jpg',
        name: 'Forever Alone',
        size: 70
    },
    // Y U NO
    {
        url: 'https://i.imgflip.com/1bgw.jpg',
        name: 'Y U NO',
        size: 80
    },
    // Me Gusta
    {
        url: 'https://i.imgflip.com/9sw2.jpg',
        name: 'Me Gusta',
        size: 70
    },
    // Rage Face
    {
        url: 'https://i.imgflip.com/1bij.jpg',
        name: 'Rage Face',
        size: 70
    },
    // Bitcoin logo (2011 era)
    {
        url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/200px-Bitcoin.svg.png',
        name: 'Bitcoin',
        size: 60
    },
    // Doge (early version)
    {
        url: 'https://i.imgflip.com/4t0m5.jpg',
        name: 'Doge',
        size: 80
    },
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
