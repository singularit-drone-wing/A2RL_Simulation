import numpy as np
import mujoco
from crazyflow.sim import Sim
from crazyflow.control import Control


sim = Sim(n_worlds=1, n_drones=1, control=Control.state)
sim.reset()


CAMERA_WIDTH = 820
CAMERA_HEIGHT = 616
CAMERA_FOV = 90

cmd = np.zeros((1, 1, 13), dtype=np.float32)
cmd[0, 0, 2] = 0.5

sim.mj_model.vis.global_.offwidth = 820
sim.mj_model.vis.global_.offheight = 616
renderer = mujoco.Renderer(sim.mj_model, CAMERA_HEIGHT, CAMERA_WIDTH)

print(f"Camera simulation started!")
print(f"Resolution: {CAMERA_WIDTH}x{CAMERA_HEIGHT}")
print(f"Field of view: {CAMERA_FOV} degrees")
print("-" * 50)

for step in range(20):
    sim.state_control(cmd)
    sim.step(sim.freq // sim.control_freq)

    renderer.update_scene(sim.mj_data, camera="fpv_cam:0")
    image = renderer.render()

    print(f"Step {step:02d} | Image shape: {image.shape} | "
          f"Min pixel: {image.min()} | Max pixel: {image.max()}")

print("-" * 50)
print("Camera simulation complete!")