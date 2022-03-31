def execute():
    try:
        from dice import dice
    except ImportError:
        import dice
    dice.run()

if __name__ == "__main__":
    execute()