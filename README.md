# 🪖 Guerilla: The Card War Game

Welcome, soldier. You are entering the world of **Guerilla** — a brutal, tactical card-based skirmish for survival, glory, and domination.

This isn't poker. This is war. And in war, every card counts. 💣

---

## 🎯 Objective

Eliminate all other players using tactical strikes, defensive maneuvers, and psychological warfare.  
Be the last survivor standing in this digital battlefield.

---

## 🂠 The Rules of Engagement

### 🃏 Deck
- The deck consists of 52 cards (1–13 for ♠, ♥, ♣, ♦).
- The King of ♦ is special — its value is **0**.
- Cards are shuffled at the start of the game.

### 🧑‍🤝‍🧑 Players
- From 2 to 8 warriors can enter the arena.
- Each is dealt 4 cards:
  - The **lowest** becomes their 🛡️ **defense**
  - The other 3 are their ❤️ **hit points (HP)**

### 🎮 Actions per turn
Each turn, a player may:

1. **Attack** another player  
   Draw a card → compare to target’s defense → deal excess as damage.

2. **Charge**  
   Prepare an extra card to empower your next attack.  
   *Warning: charging disables attacking until the next turn.*

3. **Change Defense**  
   Draw a new defense card — for yourself or any player (friend or foe).  
   Old defense is discarded back into the deck.

---

## 💀 Death & Survival

When HP drops to 0 or below:

🪙 The player gets **one last chance** —  
Guess the shape (♠, ♥, ♣, ♦) of the next drawn card.

- If guessed right → *"CHEATED DEATH"* 🧟
- If guessed wrong → *"FELL IN BATTLE"* ☠️

---

## 🤖 Bot Players

Bots are trained soldiers with their own strategies.

### 🤖 Available Bot Types:
- `RandomBotPlayer`:  
  Makes random decisions each turn.  
  *Chaotic. Unpredictable. Dangerous in numbers.*

(Coming soon: AlphaBetaBot, RLBot...)

---

## 🛠 How to Run the Game

1. 🔧 Clone the project:

```bash
git clone https://github.com/8Raouf24/guerilla
cd guerilla

2. 🐍 Run the game:
python3 game.py


3. ☠️ Choose the number of players (2–8)

4. 🧠 Choose the number of Bots (you can similate a game between bots only).
