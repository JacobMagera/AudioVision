# Choices
***
## Project Direction
At first my project was entirely different, but as time dwindled I found that I did not own the sensor necessary to bring my vision to life.
This was where I faced my first major cross-roads: To go out and look for this (potentially elusive) sensor at a shop, or to switch direction.
While I was passionate about my initial project, I ended up deciding to switch. I realized that I could explore the aforementioned project
at a later date and work on something a bit more manageable in the timeframe I had. I looked at the list of sensors that I *do* have, and saw
the Ultrasonic Ranging Module, and instantly I thought about the potential application in the medical field in helping visually impaired individuals.
Influenced by the concept of echolocation used by bats, I was set on using sound to bring a sense of sight back to the sightless.

## Audio Change
At this point it was clear that the output of the buzzer needed to change based on the distance, and that left me with three options:
Either I could change the volume of the beeps, the pitch of the beeps or the frequency of the beeps. The first option seemed to be a good idea,
but after further inspection it turned out to be unrealistic, since changing the volume of the buzzer would require changing the amplitude of the current
being channeled into the it, which is not feasible with the materials I had on hand. The second option was quickly turned down as well, since the buzzer 
simply doesn't change in pitch. That left me with the third option, which was doable with methods from the GPIOD class.

## Portability
Next came the issue of portability and setup. I wanted the device to be portable, but then rose the issue of setup. The obvious choice is to have an on/off 
button for the script on the breadboard which allows for the beeping to be paused and unpaused, but then comes the issue of power. Given this solution,
the program would stop working altogether if the RaspberryPi lost power, and the script would have to be reopened through SSH or VNS, or even worse through
connecting to a monitor! So how could I make it so that the script functions even after losing power? Although it isn't a simple solution, I decided to
have the script run automatically anytime the RaspberryPi is rebooted! Since the RaspberryPi doesn't have a power button, it boots as soon as it recieves power.
This way, I just needed to figure out a way to shut off the RaspberryPi *without* causing damage to it. Unplugging a machine while it is running can cause
corruption and other damage. So how would I have it shut off without damaging it?? That is when I remembered that you can run system commands within your python
code. Perfect solution! I attached a button to the breadboard which, when pressed, entered "sudo shutdown -h now" and powered off the RaspberryPi. I then
created a shell script responsible for executing the python script, and had that shell script added to crontab, making it start automatically on reboot.
That way, when you want to use the AudioVision, you only need to power your RaspberryPi and you do not have to worry about configuration.
