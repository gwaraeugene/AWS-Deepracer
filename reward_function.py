def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    progress = params['progress']

    TOTAL_NUM_STEPS = 10
    if (steps % 100) == 0 and progress > (steps/TOTAL_NUM_STEPS) * 100:
        reward += 10

    # Calculate 6 markers that are at varying distances away from the center line
    marker_1 = 0.01 * track_width
    marker_2 = 0.09 * track_width
    marker_3 = 0.2 * track_width
    marker_4 = 0.25 * track_width
    marker_5 = 0.3 * track_width
    marker_6 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if all_wheels_on_track and distance_from_center <= marker_1:
        reward = 1.0
    elif all_wheels_on_track and distance_from_center <= marker_2:
        reward = 0.79
    elif all_wheels_on_track and distance_from_center <= marker_3:
        reward = 0.68
    elif all_wheels_on_track and distance_from_center <= marker_4:
        reward = 0.6
    elif all_wheels_on_track and distance_from_center <= marker_5:
        reward = 0.55
    elif all_wheels_on_track and distance_from_center <= marker_6:
        reward = 0.35
    else:
        reward = 1e-3 # likely crashed/ close to off track

    return float(reward)
