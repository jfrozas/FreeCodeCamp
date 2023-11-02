# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_history={}):
  counter = {'P': 'S', 'R': 'P', 'S': 'R'}
  
  if prev_play != "":
    opponent_history.append(prev_play)
  
  prediction = 'P'

  number_plays_stored = 5
  
  if len(opponent_history) > number_plays_stored:
    last_n_plays_stored = "".join(opponent_history[-number_plays_stored:])
    last_n_plays_stored_plus1 = "".join(opponent_history[-(number_plays_stored+1):])

    play_history[last_n_plays_stored_plus1] = play_history.get(last_n_plays_stored_plus1, 0) + 1
    
    potential_plays = [last_n_plays_stored + "R",last_n_plays_stored + "S",last_n_plays_stored + "P"]

    for i in potential_plays:
      play_history.setdefault(i, 0)

    prediction = max(potential_plays, key=play_history.get)[-1]

  return counter[prediction]