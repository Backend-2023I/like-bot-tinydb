# Like-bot for TinyDB database

## Creteate new environment

```bash
python3 -m venv venv
```

## Activate environment

```bash
source venv/bin/activate
```

## Activate environment for Windows

```bash
venv/Scripts/activate
```

## Create requirements.txt .gitignore

```bash
touch requirements.txt .gitignore
```

## Install requirements

```bash
pip install -r requirements.txt
```

## export TOKEN eniviron variable

```bash
export TOKEN=your_token
```

## Database with TinyDB

```json
{
    "__default": {
        "user1":{
            "like": 0,
            "dislike": 0
        },
        "user2":{
            "like": 0,
            "dislike": 0
        }
    }
}
```
