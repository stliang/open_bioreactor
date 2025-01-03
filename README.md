# open_bioreactor

## Basic Bioreactor

### Bill of Materials:

[Atlas Scientific pH sensor value range 2 to 13](https://atlas-scientific.com/probes/consumer-grade-ph-probe/?srsltid=AfmBOoq2XOZbP1kmpz-C4iFq7Nv2fGiThBVZO9XP4gi5kphyvKDB14lt)

[Atlas Scientific temperature sensor value range -200 ̊C to 850 ̊C](https://atlas-scientific.com/probes/pt-1000-temperature-probe/?srsltid=AfmBOoqnRVyS8YNneWWp-LkBQtsg7kMbxR1cmp_p6hYV2G-46r9LpD-E)

### Guide to help you get started step-by-step:

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

# Exsample projects:

Biofertilizers and Soil Health
Rhizobium:

Benefits: Fixes atmospheric nitrogen into soil for legumes.
Applications: Used as biofertilizers for crops like beans, peas, and lentils.
Azospirillum:

Benefits: Promotes plant root growth and fixes nitrogen.
Applications: Used in cereal crops like maize and wheat.
Bacillus subtilis:

Benefits: Protects plants by suppressing pathogens and promotes plant growth.
Applications: Used as a biocontrol agent and in biofertilizers.
Pseudomonas fluorescens:

Benefits: Suppresses soil-borne diseases and promotes root health.
Applications: Used in agriculture to protect crops and improve yields.


# Producing Rhizobium

Producing Rhizobium bacteria involves cultivating the bacteria under controlled conditions, scaling up the culture, and preparing it for use as a biofertilizer. Here’s a step-by-step guide for producing Rhizobium:

Step 1: Preparation
Choose the Rhizobium Strain:

Obtain a specific strain suitable for the target crop (e.g., Rhizobium leguminosarum for peas or Rhizobium japonicum for soybeans).
You can source it from an agricultural research center or microbiology lab.
Prepare the Growth Medium:

Rhizobium grows well in a yeast mannitol broth (YMB) or yeast mannitol agar (YMA) medium.
YMB Recipe (per liter of distilled water):
Mannitol: 10 g
Yeast extract: 0.5 g
Dipotassium phosphate (K₂HPO₄): 0.5 g
Magnesium sulfate (MgSO₄·7H₂O): 0.2 g
Sodium chloride (NaCl): 0.1 g
Adjust pH to 6.8-7.0 using NaOH or HCl.
Sterilize:

Autoclave the medium at 121°C (15 psi) for 15-20 minutes to prevent contamination.
Step 2: Inoculation
Prepare Inoculum:

Use a pure culture of Rhizobium obtained from a reliable source.
Inoculate the Medium:

Transfer the pure culture into the sterilized liquid medium under aseptic conditions (e.g., in a laminar flow hood).
Incubate:

Incubate the culture at 28-30°C for 5-7 days in a shaking incubator (150-200 RPM) to ensure proper aeration and growth.
Monitor the growth visually (the broth should become turbid) or measure optical density (OD) at 600 nm using a spectrophotometer.
Step 3: Scale-Up Production
Prepare Larger Volumes:

Once the initial culture has grown, use it to inoculate larger volumes of the medium in the bioreactor or fermenter.
Monitor Growth Conditions:

Maintain a temperature of 28-30°C.
Provide gentle aeration (if using a bioreactor) to avoid harming the bacteria.
Maintain sterile conditions to avoid contamination.
Harvest the Culture:

Once the culture reaches its exponential growth phase (maximum cell density), it is ready to be harvested.
Step 4: Formulate the Biofertilizer
Prepare the Carrier Material:

Use sterilized peat, lignite, or other organic materials as carriers to protect the bacteria and ensure their viability.
Sterilize the carrier by autoclaving or using gamma irradiation.
Mix the Culture with Carrier:

Add the Rhizobium culture to the sterilized carrier in a mixing chamber.
Ensure the mixture is homogenous.
Curing:

Air-dry the mixture under sterile conditions at room temperature for 24-48 hours.
Packaging:

Pack the mixture into sterile polyethylene bags or pouches.
Label the packages with details such as the strain, target crop, and expiration date.
Step 5: Quality Control
Check Viability:
Test the population density of Rhizobium (should be at least 10⁷-10⁸ cells per gram of carrier).
Sterility Test:
Check for contamination using agar plates or microscopy.
Efficacy Test:
Test the biofertilizer by inoculating legume plants and observing nodulation.
Step 6: Application
Apply the Rhizobium biofertilizer by seed coating or directly to the soil:
Seed Coating: Mix the biofertilizer with seeds using a sticking agent (e.g., 10% sugar solution).
Soil Application: Mix the biofertilizer with compost or soil and apply it to the planting area.
Equipment Needed
Sterilization equipment (autoclave).
Shaking incubator or bioreactor.
Laminar flow hood for aseptic inoculation.
Spectrophotometer for monitoring growth.
Mixer for carrier preparation.
This process ensures you produce high-quality Rhizobium for agricultural use, enhancing nitrogen fixation and promoting plant growth.

Here are some places to get Rhizobium leguminosarum:
Carolina Biological: Sells living Rhizobium leguminosarum in tubes 
Amazon: Sells rhizobium inoculants 
VWR: Sells live Rhizobium leguminosarum cultures, but requires business documentation to purchase 
Ward's: Sells live Rhizobium leguminosarum cultures, but some items may have specific temperature and storage requirements 


## Backend Systems

### Installing Ansible on a Raspberry Pi
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

### Install Promethus
Use homebrew to install Promethus on MacOS
Configure Promethus
```
vi /opt/homebrew/etc/prometheus.yml

global:
  scrape_interval: 300s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
    - targets: ["localhost:9090"]
  - job_name: "atlas_scientific_sensors"
    static_configs:
    - targets: ["192.168.1.147:5000"]
```

Restart Promethus
```
brew services restart prometheus
```


TODOs
* Write a python 3 script to automate the setup PXE Boot server for Raspberry Pi
* If there is automation gap PXE left, then write a python 3 script to automate ansible setup for Raspberry Pi

## Reference
* [full example](https://qmacro.org/blog/posts/2020/04/05/initial-pi-configuration-via-ansible/)
* [git repo](https://github.com/mkuthan/raspberry-ansible)
* [simple example](https://medium.com/@tisutisu/installing-ansible-on-a-raspberry-pi-cc3ea79edc05)
* [PXE Boot](https://www.howtoraspberry.com/2022/03/how-to-pxe-boot-a-raspberry/)
