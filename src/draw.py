import math
class BoardDrawer():

    # Reversed/mirrored characters dictionary
    mirror_map = {
        'A': 'Ɐ',
        '2': 'ᘔ',
        '3': 'Ɛ',
        '4': '߈',
        '5': 'ဌ',
        '6': '9',  # 6 and 9 are flipped
        '7': 'ㄥ',
        '8': '8',
        '9': '6',
        'J': 'ᒋ',  # or just 'Ʝ' but less readable
        'Q': 'Ό',  # Approximate
        'K': 'ꓘ'
    }


    @classmethod
    def mirror_char(self,c):
        return self.mirror_map.get(c, c)
    

    @classmethod
    def value_to_symbol(self,value):
        if value == 0:
            return 'K'
        elif value == 1:
            return 'A'
        elif value == 11:
            return 'J'
        elif value == 12:
            return 'Q'
        elif value == 13:
            return 'K'
        else:
            return str(value)
        

    @classmethod
    def shape_to_symbol(self,shape):
        symbols = {
            'heart': '♥',
            'spade': '♠',
            'club': '♣',
            'diamond': '♦'
        }
        return symbols.get(shape, '?')


    @classmethod
    def format_card(self, card):
        value = self.value_to_symbol(card['value'])
        mirrored_value = ''.join(self.mirror_char(c) for c in value)
        shape = self.shape_to_symbol(card['shape'])

        # Top value normal, bottom value mirrored
        return [
            f"┌──────┐",
            f"| {value:<2}{shape}  |",
            f"|      |",
            f"|  {shape}{mirrored_value:>2} |",
            f"└──────┘"
        ]
    
    @classmethod
    def draw_full_board(self, players):
        nb_players = len(players)
        top_nb = math.ceil(nb_players / 2)
        
        bottom_nb = nb_players - top_nb
        

        top_players = players[:top_nb]
        bottom_players = players[top_nb:]

        # Draw top players
        self.draw_row(top_players, is_top=True)
        print("\n" * 2)  # Space between top and bottom
        self.draw_row(bottom_players, is_top=False)

    @classmethod
    def draw_row(self, players, is_top=True):
        if not players:
            return

        spacing_between_players = " " * 10
        card_width = 8
        space_between_cards = 1
        cards_per_player = 3
        player_block_width = (card_width * cards_per_player) + (space_between_cards * (cards_per_player - 1))

        # Prepare full player blocks
        players_blocks = []
        players_names = []
        for player in players:
            defense_card = player.defense_card
            hp_cards = player.hp_cards

            # Draw HP cards horizontally
            hp_lines = [self.format_card(card) for card in hp_cards]
            hp_block = [
                ' '.join(card[i] for card in hp_lines)
                for i in range(5)
            ]

            # Draw defense card normally
            defense_lines = self.format_card(defense_card)

            # Calculate true HP line width
            hp_line_width = len(hp_block[0])

            # Center defense card under or above HP cards
            pad_size = (hp_line_width - card_width) // 2
            padded_defense = [' ' * pad_size + line + (' ' * pad_size)  for line in defense_lines]

            # Merge the block for the player
            if is_top:
                block = hp_block + padded_defense
            else:
                block = padded_defense + hp_block

            players_blocks.append(block)

            # Center player name under block
            name = player.name
            spaces_before = (hp_line_width - len(name)) // 2
            centered_name = ' ' * spaces_before + name + ' ' * spaces_before
            players_names.append(centered_name)

        nb_lines_per_player = len(players_blocks[0])

        # Print names if top
        if is_top:
            print(spacing_between_players.join(players_names))

        for line_idx in range(nb_lines_per_player):
            row = spacing_between_players.join(player[line_idx] for player in players_blocks)
            print(row)

        # Print names if bottom
        if not is_top:
            print(spacing_between_players.join(players_names))