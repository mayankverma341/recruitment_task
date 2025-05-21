from environment import maze
from qlearning import Agent
import pickle


env = maze('C:/Users/nv909/Downloads/V1.txt')
agent = Agent(actions=[0, 1, 2, 3])

success_count,rewards = 0, []

episodes = 100000

for episode in range(episodes):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward

    agent.decay_epsilon()
    agent.save()

    rewards.append(total_reward)
    if reward > 0:
        success_count += 1
    else:
        success_count = 0

    print(f"Episode {episode} | Total Reward: {total_reward} | Streak: {success_count}")
    if success_count >= 10:
        print("Harry escaped successfully 10 times in a row")
        break

with open('metrics.pkl', 'wb') as f:
    pickle.dump((rewards, success_count), f)

