# <p align="center"> Traffic Reliever for Ambulances <p>

## Idea

The Ambulance Traffic Relief System is aimed at improving emergency response times by dynamically adjusting traffic signals to prioritize ambulances. When an ambulance is approaching a traffic signal, the system detects its proximity and automatically changes the signal to green, allowing the ambulance to pass through without delay. This helps reduce the time it takes for ambulances to reach their destinations during emergencies, potentially saving lives.

## Approach

The project utilizes a simulation environment where an ambulance is represented as a moving object on a grid-based map. Traffic signals are placed at various intersections on the map, and when the ambulance approaches a signal, the system detects its proximity and triggers the signal to turn green. This is achieved by continuously monitoring the distance between the ambulance and the signals and updating the signal status accordingly.

## Demo Video

<video width="640" height="360" controls>
  <source src="demo_video.mp4" type="video/x-matroska">
  Your browser does not support the video tag.
</video>

## Remaining Tasks

### Features to Implement
- [ ] Demo Video 
- [ ] Direction of ambulance + distance from traffic signal = Green Light 
- [ ] Implement a reset

### Bug Fix
- [ ] Ambulance shouldn't go on black line

### Automation
- [ ] Automate the script 
- [ ] Conduct usability testing with real users to gather feedback

### Optional 

- [ ] RNN if wanted

