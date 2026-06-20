import numpy as np
from crazyflow.sim import Sim
from crazyflow.control import Control

sim = Sim(n_worlds=1, n_drones=1, control=Control.state)
sim.reset()

cmd = np.zeros((1, 1, 13), dtype=np.float32)
cmd[0, 0, 2] = 0.5

prev_vel = np.array(sim.data.states.vel[0, 0])
dt = 1.0 / sim.freq

print("Step | Position (x,y,z) | Acceleration (x,y,z) | Angular Velocity (x,y,z) | Orientation (quat)")
print("-" * 100)

for step in range(20):


    sim.state_control(cmd)
    sim.step(sim.freq // sim.control_freq)

    pos      = np.array(sim.data.states.pos[0, 0])
    vel      = np.array(sim.data.states.vel[0, 0])
    ang_vel  = np.array(sim.data.states.ang_vel[0, 0])
    quat     = np.array(sim.data.states.quat[0, 0])

    accel = (vel - prev_vel) / dt
    prev_vel = vel

    imu_data = {
        "acceleration":    accel,
        "angular_velocity": ang_vel,
        "orientation":     quat,
    }

    print(f"  {step:02d} | "
          f"pos=({pos[0]:.2f},{pos[1]:.2f},{pos[2]:.2f}) | "
          f"accel=({accel[0]:.2f},{accel[1]:.2f},{accel[2]:.2f}) | "
          f"ang_vel=({ang_vel[0]:.2f},{ang_vel[1]:.2f},{ang_vel[2]:.2f}) | "
          f"quat=({quat[0]:.2f},{quat[1]:.2f},{quat[2]:.2f},{quat[3]:.2f})")

print("-" * 100)
print("IMU simulation complete!")