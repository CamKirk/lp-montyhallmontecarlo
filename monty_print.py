import pandas as pd

def print_values(results):
    """Prints values for sim to terminal window

    Args:
        results (list[trial]): list of trials to calculate.
            Expect trial as [prior:str, posterior:str,win:boolean]

    """
    # generate df

    df = pd.DataFrame(results)
    df = df.rename(columns={0:"Prior", 1:"Posterior",2:"Result" })




    # Print distribution of Priors and Posteriors

    print("""
    Distribution of Prior Selections p(A)
    """)
    print(df.groupby("Prior").count()["Result"])

    print("""
    Distribution of Posterior Selections 
    Note, this is NOT the distribution of WINNING,
    only the rate at which each value is selected
    """)
    print(df.groupby(["Prior", "Posterior"]).count()["Result"])



    # Print Wins, Losses, and Winning Rate

    winrate_series = df.groupby(["Result"]).count()["Posterior"]

    print(f"""
        Wins:{winrate_series[1]} 
        Losses: {winrate_series[0]} 
        Winrate: {winrate_series[1]/(winrate_series[1]+winrate_series[0])}
        """)
    # print(df)