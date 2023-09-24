import random

nouns = ['heart', 'dream', 'time', 'love', 'flower', 'sun', 'moon', 'ocean', 'star', 'song', 'bird', 'tree', 'kiss', 'smile', 'tear', 'hope', 'wind', 'cloud', 'silence', 'shadow', 'light', 'dreamer', 'soul', 'world', 'night', 'day', 'fire', 'rain', 'snow', 'heartache', 'whisper', 'echo', 'path', 'mirror', 'mist', 'fear', 'beauty', 'color', 'dreams', 'butterfly', 'thunder', 'dawn', 'dusk', 'reflection', 'eternity', 'moment', 'dance', 'adventure', 'imagination', 'horizon', 'memory', 'river', 'bridge', 'journey', 'laughter', 'echo', 'infinity', 'laughter', 'compassion', 'melody', 'harmony', 'serenity', 'freedom', 'spark', 'twilight', 'fantasy', 'grace', 'desire', 'destiny', 'whisper', 'cascade', 'serenade', 'fragrance', 'inspiration', 'maze', 'alchemy', 'enchanted', 'glimmer', 'paradise', 'whirlwind', 'cascade', 'lullaby', 'fable', 'passion', 'cascade', 'serenade', 'rhythm', 'wonder', 'serenity', 'treasure', 'miracle', 'whirlwind', 'whisper', 'solitude', 'grace', 'innocence', 'legend']

verbs = ['dances', 'sings', 'cries', 'smiles', 'whispers', 'shines', 'sleeps', 'awakens', 'cries', 'laughs', 'melts', 'fades', 'blooms', 'wanders', 'glimmers', 'glows', 'fades', 'flies', 'echoes', 'reflects', 'ignites', 'flickers', 'travels', 'envelopes', 'echoes', 'dissolves', 'resonates', 'yearns', 'soars', 'savors', 'weaves', 'flourishes', 'softens', 'sails', 'sways', 'roams', 'reverberates', 'cascades', 'spins', 'fades', 'breaks', 'swims', 'drifts', 'vanishes', 'illuminates', 'falls', 'ascends', 'descends', 'transcends', 'guides', 'calls', 'tangles', 'ascends', 'settles', 'embraces', 'wanders', 'captivates', 'whirls', 'surfaces', 'haunts', 'whirls', 'glistens', 'shimmers', 'captures', 'gathers', 'caresses', 'endures', 'chases', 'rises', 'graces', 'touches', 'lingers', 'envelops', 'meanders', 'unfolds', 'departs', 'cherishes', 'basks', 'shatters', 'illuminates', 'glides', 'flickers', 'envelops', 'abides', 'resides']

adjectives = ['beautiful', 'gentle', 'mysterious', 'fragrant', 'sparkling', 'velvet', 'sacred', 'silken', 'golden', 'crimson', 'whispering', 'eternal', 'tender', 'shimmering', 'captivating', 'fleeting', 'serene', 'sublime', 'elusive', 'enchanted', 'surreal', 'heavenly', 'celestial', 'mystical', 'radiant', 'blissful', 'ethereal', 'mesmerizing', 'enchanting', 'enigmatic', 'transient', 'delicate', 'ephemeral', 'whimsical', 'soothing', 'cosmic', 'vibrant', 'magical', 'radiant', 'tranquil', 'whirlwind', 'luminous', 'mysterious', 'glorious', 'ephemeral', 'ethereal', 'tender', 'graceful', 'poignant', 'captivating', 'profound', 'dazzling', 'glimmering', 'intricate', 'glowing', 'distant', 'forgotten', 'divine', 'enraptured', 'lovely', 'mystified', 'intoxicating', 'splendid', 'wondrous', 'bewitching', 'awe-inspiring', 'resplendent', 'enveloping', 'harmonious', 'bewildering', 'majestic', 'captivated', 'invigorating', 'sensuous', 'evanescent', 'iridescent', 'entrancing', 'alluring', 'spellbinding', 'captured', 'transcendent', 'suspended', 'sublime', 'ethereal', 'melodic', 'vivid', 'graceful', 'gossamer', 'hypnotic', 'delightful', 'enlivening', 'wistful']

def generate_poem():
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)

    poem = f"The {adjective} {noun} {verb} in the moonlight."

    return poem

if __name__ == "__main__":
    poem = generate_poem()
    print(poem)

