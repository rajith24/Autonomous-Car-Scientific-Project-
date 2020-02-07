# Simulation of autonomous car in ROS and Gazebo

This project is motivated by the idea of learning the tools and the environment to simulate
autonomous vehicles. The concepts used are pretty basic and it can be learnt from sources on the internet.
The objectives that are covered in our project are :
  * To investigate the available methods to simulate autonomous vehicles
  * To build an environment (circuit track) in Gazebo
  * To find a car model to use in the environment (URDF File)
  * To launch the environment along with the car
  * To investigate image processing techniques for a lane follower in turtlebot3
  * To implement the working algorithm used on turtlebot3 in our car model
  
  
## Tools Used in this project :

 * Python
 * ROS (Robot Operating System)
 * Turtlebot3 
 * OpenCV
 * Gazebo
 * Tensorflow and Keras frameworks
 
 
## The initial proof of concept approach

The turtlebot3 autorace environment was used to implement code snippets to verify performance and the use of logic.
The whole project is aimed at making a lane tracker, or I would say it is a sophisticated version of a line follower.

The aim of the project is to keep the bots aligned on track while it navigates towards its destination.
The turtlebot3 autorace environment was an ideal playground to learn the various concepts and to navigate around the
ROS environment.


## The gist of the algorithm/approach

 * Subscribe and Publish to relevent and required topics like camera, laserscanner, velocity publisher etc.
 * Crop out the most impactful region of the image to reduce the burden of computation
 * To create an upper and lower hsv masks for filtering out the colors which we are interested
 * Obtaining the moments for the tracked colors (used to calculate the centre of concentration/mass of the color)
 * To make a proportional control of the velocity control so that it keeps the error of the centre of camera to the centroid to be minimal or ideally zero. This is basically an attempt to keep the color to be tracked at the centre of the screen always and hence adjusting the bot to move in accordance to this criteria.
 * This same exact concept is applied to a Prius model on a simple environment which was created in Gazebo.
 * The only differences in the application to the Prius model is the means of control and the access to topics published by the Prius Model.
 
The descriptions above are really pretty minimal and you can look into the codes and the world files if you are interested in learning ROS and doing a project to do so.

 ## Video snippets of the project
 You can look at some visuals on these links :
 
  * [Turtlebot3 Implementation](https://drive.google.com/open?id=1eXp8JXX_nMk8hKcOad40VWAnxlkcOK0g)
  * [Prius Model Implementation video 1](https://drive.google.com/open?id=1r1abV36PSdVPBGdf2UOIe3D0sQ3h5-Ss) 
  * [Prius Model Implementaition video 2](https://drive.google.com/open?id=1wsNgyoLenB_CRfIaCOn0R98JcfnWogUx)
   
 
 
