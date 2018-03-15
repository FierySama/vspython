team = input('Enter your favorite hockey team: ').upper()
sport = input('Enter your favorite sport: ').upper()

sportIsHockey = False
if sport == 'HOCKEY':
    sportIsHockey = True

teamIsCorrect = False
if team == 'SENATORS' or team == 'LEAFS':
    teamIsCorrect = True

if sportIsHockey and teamIsCorrect:
    print('good luck getting to the cup this year')

# if the sport is hockey, and the team is the senators or leafs, display cup message
# AND StATEMENt IS oVERRIDING EVERYTHING
if sport == 'HOCKEY' and (team == 'SENATORS' or team == 'LEAFS'):
    print('Good luck getting to the cup this year ')


# if sport == 'HOCKEY' and team == 'RANGERS':
#     print('I miss messier')
# elif team == 'LEAFS' or team == 'SENATORS':
#     print('Good luck getitng the cup this year')
# else:
#     print('I don't know that team ')

# if team == 'FLYERS':
    #     print('Best team ever!! ')
    # elif team == 'SENATORS':
    #     print('Go sens go! ')
    # elif team == 'RANGERS':
    #     print('Go rangers ')
    # else:
    #     print('I don\'t have anything clever to say but hell, we're programming in python! ')
