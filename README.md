# Sneakers price tools

## Tools:

* Price checker : *Search for a sneaker and return the payouts*
  * Stockx (highest bid payouts)
  * Restocks (highest resell payouts)
  * FlightClub (highest consignement payouts)

#### Example :

*Type the command for the site you want*
![command](./assets/command.png)

*Select a sneaker based on your research*
![menu](./assets/menu.png)

*Get the payouts*
![payouts](./assets/payouts.png)
## Configuration

### Environnement

create .env file
```dotenv
DISCORD_TOKEN=""
# Restocks
RESTOCKS_EMAIL=""
RESTOCKS_PASSWORD=""
```

### Dependencies

install project dependencies

```bash
pipenv sync --dev
```

## How to run

```bash
python main.py &
```

### Contact

* MichelRebel#4821
* [Twitter](https://twitter.com/keskonsmare)