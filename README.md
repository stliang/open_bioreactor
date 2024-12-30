# open_bioreactor

## Basic Bioreactor

Bill of Materials:

[Atlas Scientific pH sensor value range 2 to 13](https://atlas-scientific.com/probes/consumer-grade-ph-probe/?srsltid=AfmBOoq2XOZbP1kmpz-C4iFq7Nv2fGiThBVZO9XP4gi5kphyvKDB14lt)

[Atlas Scientific temperature sensor value range -200 ̊C to 850 ̊C](https://atlas-scientific.com/probes/pt-1000-temperature-probe/?srsltid=AfmBOoqnRVyS8YNneWWp-LkBQtsg7kMbxR1cmp_p6hYV2G-46r9LpD-E)

Here’s a step-by-step guide to help you get started:

Materials Needed
Vessel

Glass carboy, Erlenmeyer flask, or any other suitable container (1-2 liters capacity)
Agitation System

Magnetic stirrer or overhead stirrer with impellers
Aeration System

Air pump (aquarium air pump can work)
Air tubing
Sparger (could be a simple glass or stainless steel sparger)
Temperature Control

Heating mantle or water bath
Thermometer or temperature probe
pH Control

pH meter or pH indicator strips
Acid/base solutions for adjustments
Additions and Sampling

Sterile syringes or pipettes
Tubing for nutrient feed and sampling
Stepper Motor Controller (Optional)

For automated stirring
Step-by-Step Guide
1. Setup the Vessel
Choose a clean and sterile vessel such as a glass carboy or an Erlenmeyer flask. Ensure it has an opening to add the components.

2. Assemble the Agitation System
If using a magnetic stirrer, place the magnetic stir bar inside the vessel and use a magnetic stir plate to adjust the speed.
For an overhead stirrer, mount the stirrer on top of the vessel and adjust the impellers for optimal mixing.
3. Configure the Aeration System
Air Pump: Connect the air pump to the sparger using air tubing. Make sure to sterilize the sparger before placing it into the vessel.
Sparger Placement: Insert the sparger into the vessel in such a way that it sits near the bottom to adequately aerate the culture.
4. Temperature Control
Use a thermometer or temperature probe to monitor the temperature.
If using a heating mantle, wrap it around the vessel or submerge the vessel in a water bath.
Adjust the temperature according to the organism’s optimal growth conditions.
5. pH Control
Monitor the pH using either a pH meter or pH indicator strips.
Adjust pH by adding small amounts of acid (e.g., hydrochloric acid) or base (e.g., sodium hydroxide) as needed.
6. Nutrient Addition and Sampling
Use sterile syringes or pipettes for sterile addition of nutrients and for sampling.
Have tubing in place for regular feeding of nutrients if performing a fed-batch process.
Optional: Automation and Controls
Stepper Motor: For automated and more precise stirring.
Arduino or Raspberry Pi: For automating monitoring and control of temperature, pH, and aeration.
Maintenance and Operation Tips
Sterilization: Always sterilize your vessel and components before starting the culture to avoid contamination.
Monitoring: Regularly check the pH, temperature, and dissolved oxygen levels.
Sampling: Take regular samples to monitor the growth and health of your culture.

## Installing Ansible on a Raspberry Pi
Assumptions:
1.) Running on Raspberry Pi 4+
```
sudo cat /sys/firmware/devicetree/base/model;echo
sudo apt update
sudo apt install -y software-properties-common
sudo apt install -y ansible
ansible --version 
```

Setup Log
```
id
clear
cd /etc/
sudo mkdir ansible
sudo vi /etc/ansible/ansible.cfg
sudo vi /etc/ansible/hosts
cat /etc/ansible/hosts 
ping 192.168.1.147
ansible myservers -m ping -u pi --ask-pass
which sshpass
```

TODOs
* Write a python 3 script to automate the setup PXE Boot server for Raspberry Pi
* If there is automation gap PXE left, then write a python 3 script to automate ansible setup for Raspberry Pi

## Reference
* [full example](https://qmacro.org/blog/posts/2020/04/05/initial-pi-configuration-via-ansible/)
* [git repo](https://github.com/mkuthan/raspberry-ansible)
* [simple example](https://medium.com/@tisutisu/installing-ansible-on-a-raspberry-pi-cc3ea79edc05)
* [PXE Boot](https://www.howtoraspberry.com/2022/03/how-to-pxe-boot-a-raspberry/)
