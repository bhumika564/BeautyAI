from utils import render_layout
from components.hero import hero
from components.stats import stats
from components.features import features
from components.trending import trending

def home_content():
    hero()
    stats()
    features()
    trending()

def main():
    render_layout(home_content, "Home")

if __name__ == "__main__":
    main()
