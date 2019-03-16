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

    # abstract groupby calls

    prior_group = df.groupby("Prior")
    posterior_group = df.groupby(["Prior", "Posterior"])



    # Print distribution of Priors and Posteriors

    print("""
    Distribution of Prior Selections p(A)
    """)
    print(prior_group.count()["Result"])

    print("""
    Distribution of Posterior Selections 
    Note, this is NOT the distribution of WINNING,
    only the rate at which each value is selected
    """)
    print(posterior_group.count()["Result"])



    # Print Wins, Losses, and Winning Rate

    print("Data on wins")

    winrate_series = df.groupby(["Result"]).count()["Posterior"]

    print(f"""
        Wins:{winrate_series[1]} 
        Losses: {winrate_series[0]} 
        Winrate: {winrate_series[1]/(winrate_series[1]+winrate_series[0])}
        """)

    # Wins by Prior
    
    print("""
    Wins by Prior Selection
    """)

    prior_win_df = prior_group.count().join(prior_group.sum(), rsuffix="win")
    prior_win_df.rename(inplace=True, columns={"Result":"Trials", "Resultwin":"Wins"})
    prior_win_df = prior_win_df[["Trials","Wins"]]
    prior_win_df["Winrate"] = prior_win_df["Wins"]/prior_win_df["Trials"]
    print(prior_win_df)

    # Wins by Posterior

    print("""
    Wins by Posterior Selection
    """)

    posterior_win_df = posterior_group.count().join(posterior_group.sum(), rsuffix="win")
    posterior_win_df.rename(inplace=True, columns={"Result":"Trials", "Resultwin":"Wins"})
    posterior_win_df = posterior_win_df[["Trials","Wins"]]
    posterior_win_df["Winrate"] = posterior_win_df["Wins"]/posterior_win_df["Trials"]
    print(posterior_win_df)
