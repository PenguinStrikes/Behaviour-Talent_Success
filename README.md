### Talent vs. Luck Model
This project invesigates replicating the results from the paper published by A. Pluchino, A. E. Biondo, A. Rapisarda (Talent vs Luck:
the role of randomness in success and failure)

#### Launching a new environment
The following command will launch a new environment with the relevant dependencies:
```
conda env create -f environment.yml -n talent_luck
```
Once created, the new environment can be activated and deactivated using the following commands:
```
source activate talent_luck
source deactivate talent_luck
```
To remove the environment after deactivation run:
```
conda env remove -n talent_luck
```

#### Creating the Python Model
The model in the paper creates a world of people and events. The events move randomly in time and can intercept people, affecting that persons success value. A positive event doubles their success, a negative event halves their success. In **notebooks** there is an analysis python notebook which walks through setting up this world and simulating these events.

#### Python Results 