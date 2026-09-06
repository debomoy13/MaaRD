from env import simple_env

env=simple_env()

env.reset()

print("Initial Environment")
env.render()

print("Move right")
state,reward,done=env.step(3)
print("State:", state)
print("Reward:", reward)
print("Done:", done)


print("Move up")
state,reward,done=env.step(1)
print("State:", state)
print("Reward:", reward)
print("Done:", done)

print("Move right")
state,reward,done=env.step(3)
print("State:", state)
print("Reward:", reward)
print("Done:", done)

env.render()