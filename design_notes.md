# Coding the Guerilla Game

## 🛠️ Development Plan

We'll begin by listing the steps to develop the game in a chronological order.

---

## 🎮 General Rules

### 1. Deck of Cards
- Represent the deck as an array of values.
- Shuffle the deck at the start of the game.
- Cards are played from the top of the deck.
- After playing, cards are returned to the end of the deck.

### 2. Players
- Minimum: **2 players**
- Maximum: **8 players**
- Each player is dealt **4 cards** from the deck:
  - The **lowest** card becomes their **defense**.
  - The **remaining 3 cards** form the player's **HP**.
- A player is **dead once his HP goes down to 0 **.
- We must **track the specific HP cards**, as they are returned to the deck when the player takes damage.

## 🔁 Player Actions
A player can:
- **Attack** another player. He will play a card and if the value of that card is greater than the defense of the oppenent he will inflict damage to him
- **Charge** a card to launch an empowered attack in the next turn.
- **Change** the defense card of any player (Himself Included).
- **Turtle** the player can put another card in defense for 

### 3. Game rules 
- Each player starts with 4 cards 
- The player whom the sum of his cards is the lowest starts
- The last player alive wins 
