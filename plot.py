import matplotlib.pyplot as plt
import pickle

# Assume these are saved during training
with open('metrics.pkl', 'rb') as file:
    rewards, success_streaks = pickle.load(file)

plt.figure(figsize=(20, 6))

plt.subplot(1, 2, 2)
plt.plot(success_streaks)
plt.title("Success Streaks")
plt.xlabel("Episode")
plt.ylabel("Streak")

plt.subplot(1, 2, 1)
plt.plot(rewards)
plt.title("Per Episode Rewards")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.show()

