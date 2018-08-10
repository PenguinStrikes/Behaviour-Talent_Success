import numpy as np
import scipy


def talent_luck_model(n, p, t, s, evn_i, tal_x, tal_s,
                      unlucky='im',
                      interest=0):
    
    # Create talents array
    peoples_talents = np.random.normal(tal_x, tal_s, n)
    
    # Create a 2D array of people over time
    world = np.zeros((n,t+1))

    # Change each persons initial success to 10
    world[:,0] = s * 1.0

    # Iterate through each time step (0 is the initial state)
    for i in range(1,t+1):
        # Creates an array of random events occurring
        does_an_event_occur = np.random.binomial(n=1, p=evn_i, size=n)

        # Array of good or bad occurence
        is_an_event_good = np.random.binomial(n=1, p=p, size=n) * 1.0
        is_an_event_good[:] = [0.5 if x != 1 else 2 for x in is_an_event_good]

        # Combine the two arrays
        event_impact = does_an_event_occur * is_an_event_good 
        event_impact[:] = [x if x != 0 else 1 for x in event_impact]

        # Factoring in talents to positive events
        advantage = peoples_talents - np.random.rand(n)
        advantage = [1 if x > 0 else 0 for x in advantage]
        i_talent = [1 if (i == 2) & (j == 0) else i for i, j in zip(event_impact, advantage)]

        # Should talent affect the ability to protect against unlucky events?
        if unlucky == 'bal':
            i_talent = [1 if (i == 0.5) & (j == 1) else i for i, j in zip(i_talent, advantage)]
        
        # Taking the value before, multiply by the event impact and consider interest on capital
        if interest > 0:
            world[:,i] = (world[:,i-1] + (world[:,i-1] * interest)) * i_talent
        else:
            world[:,i] = world[:,i-1] * i_talent
        
    return world, world[:,t], peoples_talents