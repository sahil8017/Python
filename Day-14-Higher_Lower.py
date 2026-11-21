import random


data = [
    {
        'name': 'Instagram',
        'follower_count': 686,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 681,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 517,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 402,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 381,
        'description': 'Media personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 380,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 362,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 344,
        'description': 'Media personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 298,
        'description': 'Musician and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 291,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'Nike',
        'follower_count': 291,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 286,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 278,
        'description': 'Media personality and model',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 272,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 271,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'National Geographic',
        'follower_count': 268,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 241,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 240,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 209,
        'description': 'Media personality',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 205,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 195,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 183,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Zendaya',
        'follower_count': 178,
        'description': 'Actress and singer',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 172,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 161,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 153,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 150,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 147,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Rihanna',
        'follower_count': 146,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Drake',
        'follower_count': 140,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 140,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kylian Mbappé',
        'follower_count': 137,
        'description': 'Footballer',
        'country': 'France'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 130,
        'description': 'Comedian and television host',
        'country': 'United States'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 123,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 121,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'Narendra Modi',
        'follower_count': 107,
        'description': 'Prime Minister of India',
        'country': 'India'
    },
    {
        'name': 'Lisa',
        'follower_count': 106,
        'description': 'Musician',
        'country': 'Thailand'
    },
    {
        'name': 'NASA',
        'follower_count': 104,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 103,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Gal Gadot',
        'follower_count': 103,
        'description': 'Actress',
        'country': 'Israel'
    },
    {
        'name': 'Shakira',
        'follower_count': 103,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Priyanka Chopra',
        'follower_count': 93,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Shraddha Kapoor',
        'follower_count': 93,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'MrBeast',
        'follower_count': 91,
        'description': 'YouTuber and philanthropist',
        'country': 'United States'
    },
    {
        'name': 'Jennie',
        'follower_count': 89,
        'description': 'Musician',
        'country': 'South Korea'
    },
    {
        'name': 'Dua Lipa',
        'follower_count': 89,
        'description': 'Musician',
        'country': 'United Kingdom'
    },
    {
        'name': 'NBA',
        'follower_count': 88,
        'description': 'Professional basketball league',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 88,
        'description': 'Former footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Snoop Dogg',
        'follower_count': 87,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Alia Bhatt',
        'follower_count': 85,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Rosé',
        'follower_count': 83,
        'description': 'Musician',
        'country': 'New Zealand'
    },
    {
        'name': 'BTS',
        'follower_count': 82,
        'description': 'Musical group',
        'country': 'South Korea'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 81,
        'description': 'Former footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Premier League',
        'follower_count': 81,
        'description': 'Football league',
        'country': 'United Kingdom'
    },
    {
        'name': 'Jisoo',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'South Korea'
    },
    {
        'name': '433',
        'follower_count': 80,
        'description': 'Football media brand',
        'country': 'Netherlands'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 80,
        'description': 'Lingerie and apparel retailer',
        'country': 'United States'
    },
    {
        'name': 'Katrina Kaif',
        'follower_count': 79,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Deepika Padukone',
        'follower_count': 78,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Khabane Lame',
        'follower_count': 78,
        'description': 'Social media personality',
        'country': 'Italy'
    },
    {
        'name': 'Georgina Rodríguez',
        'follower_count': 78,
        'description': 'Model and media personality',
        'country': 'Spain'
    },
    {
        'name': 'V (BTS)',
        'follower_count': 78,
        'description': 'Musician',
        'country': 'South Korea'
    },
    {
        'name': 'The Weeknd',
        'follower_count': 77,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Erling Haaland',
        'follower_count': 77,
        'description': 'Footballer',
        'country': 'Norway'
    },
    {
        'name': 'Neha Kakkar',
        'follower_count': 76,
        'description': 'Singer',
        'country': 'India'
    },
    {
        'name': 'Raffi Ahmad and Nagita Slavina',
        'follower_count': 74,
        'description': 'Television personalities',
        'country': 'Indonesia'
    },
    {
        'name': 'Karim Benzema',
        'follower_count': 74,
        'description': 'Footballer',
        'country': 'France'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 74,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Salman Khan',
        'follower_count': 73,
        'description': 'Actor',
        'country': 'India'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 71,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Karol G',
        'follower_count': 71,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Millie Bobby Brown',
        'follower_count': 70,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Sergio Ramos',
        'follower_count': 70,
        'description': 'Footballer',
        'country': 'Spain'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 69,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 69,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Tom Holland',
        'follower_count': 69,
        'description': 'Actor',
        'country': 'United Kingdom'
    },
    {
        'name': 'Mohamed Salah',
        'follower_count': 68,
        'description': 'Footballer',
        'country': 'Egypt'
    },
    {
        'name': 'Paris Saint-Germain',
        'follower_count': 68,
        'description': 'Football club',
        'country': 'France'
    },
    {
        'name': 'Jacqueline Fernandez',
        'follower_count': 67,
        'description': 'Actress',
        'country': 'Sri Lanka'
    },
    {
        'name': 'Marcelo Vieira',
        'follower_count': 67,
        'description': 'Former footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Will Smith',
        'follower_count': 67,
        'description': 'Actor and musician',
        'country': 'United States'
    },
    {
        'name': 'FIFA World Cup',
        'follower_count': 67,
        'description': 'International football competition',
        'country': 'Switzerland'
    },
    {
        'name': 'Anushka Sharma',
        'follower_count': 67,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Urvashi Rautela',
        'follower_count': 67,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Manchester United',
        'follower_count': 66,
        'description': 'Football club',
        'country': 'United Kingdom'
    },
    {
        'name': 'Marvel',
        'follower_count': 65,
        'description': 'Entertainment brand',
        'country': 'United States'
    },
    {
        'name': 'Zlatan Ibrahimović',
        'follower_count': 65,
        'description': 'Former footballer',
        'country': 'Sweden'
    },
    {
        'name': 'Akshay Kumar',
        'follower_count': 65,
        'description': 'Actor',
        'country': 'India'
    },
    {
        'name': 'Maluma',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Vinícius Júnior',
        'follower_count': 63,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Paul Pogba',
        'follower_count': 63,
        'description': 'Footballer',
        'country': 'France'
    },
    {
        'name': 'Zara',
        'follower_count': 62,
        'description': 'Fashion retailer',
        'country': 'Spain'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Lady Gaga',
        'follower_count': 61,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Anitta',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'Brazil'
    },
    {
        'name': 'Disha Patani',
        'follower_count': 60,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Lamine Yamal',
        'follower_count': 60,
        'description': 'Footballer',
        'country': 'Spain'
    },
    {
        'name': 'Robert Downey Jr.',
        'follower_count': 59,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Bella Hadid',
        'follower_count': 59,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Juventus',
        'follower_count': 59,
        'description': 'Football club',
        'country': 'Italy'
    }
]

logo = r"""
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ 
/_____/\____/|__/|__/\___/_/
"""

vs = r"""
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""

score = 0
option_b = random.choice(data)
print(logo)
def clear_screen():
    print("\033c",end="")
while True:
    option_a = option_b
    option_b = random.choice(data)

    while option_a['follower_count'] == option_b['follower_count']:
        option_b = random.choice(data)

    print(f"Compare a: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against b: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    while True:
        guess = input("Who has more followers? Type 'a' or 'b': ").lower()
        if guess not in ['a','b']:
            print("Invalid input. Please choose between 'a' and 'b'.")
            continue
        break
    score_a = option_a['follower_count']
    score_b = option_b['follower_count']

    is_correct = (score_a > score_b and guess == 'a') or (score_a < score_b and guess == 'b')

    clear_screen()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're correct. Your score is {score}.")
    else:
        print(f"This is incorrect. Final Score is {score}.")
        break