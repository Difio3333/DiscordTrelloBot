from trello import TrelloClient
import datetime



client = TrelloClient(
    api_key='YOUR_API_KEY',
    api_secret='YOUR_TRELLO_API_SECRET',
    token = 'YOUR_TRELLO_TOKEN'
)


all_boards = client.list_boards()

def find_board_and_list(board="NAME_OF_YOUR_TRELLO_BOARD",trelloList="NAME_OF_YOUR_TRELLO_LIST"):

    i = 0
    for item in all_boards:
        if item.name == board:
            break
        i+=1

    discordBoard = all_boards[i]

    bugslist = None
    for entry in discordBoard.list_lists():
        if entry.name == trelloList:
            bugslist = entry
            break

    return bugslist

def card_Im_looking_for(card_id):
    for board in all_boards:
        for entry in board.list_lists():
            for card in entry.list_cards():
                if card.id == card_id:
                    return card

def new_card_on_trello_list(cardName=None,cardDescription=None):
    if cardName == None:
        pass
    else:
        if cardDescription == None:
            cardDescription = "You have not provided a description for this bug."
        
        card = theListImLookingFor.add_card(name=f'{cardName}',desc=f"{cardDescription}")
        card.set_description(f"{card.desc}\n\nCard ID: {card.id}")
        return card 

def change_card_on_trello_list(cardId=None,cardDescription=None):
    if cardId == None:
        pass
    else:
        try:
            
            card = card_Im_looking_for(cardId)
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d | %H:%M:%S")
            card.set_description(f"{card.desc}\n\nUpdate from ({formatted_datetime}): \n{cardDescription}")
            
            return card

        except Exception as e:
            new_card_on_trello_list(cardName="FallBack Card",cardDescription=cardDescription)
            print(e)

theListImLookingFor = find_trello_list(board="NAME_OF_YOUR_BOARD",trelloList="NAME_OF_YOUR_LIST")        