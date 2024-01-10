import os
import pandas as pd


def main():
    # read folder data name
    file_list = os.listdir("data")
    file_list.sort()

    pre_df = pd.read_csv(f"data/{file_list[0]}")
    pre_df = pre_df[["Username", "Total Score"]]
    pre_df["Total Score"] = (
        pre_df["Total Score"] / (pre_df["Total Score"].max() / 100)
    ).round(2)

    # rename column
    pre_df.rename(columns={"Total Score": "HW1_score"}, inplace=True)

    for idx in range(1, len(file_list)):
        # read csv data
        df = pd.read_csv(f"data/{file_list[idx]}")
        df = df[["Username", "Total Score"]]

        # calculate avg score
        df["Total Score"] = (
            df["Total Score"] / (df["Total Score"].max() / 100)).round(2)
        df.rename(columns={"Total Score": f"HW{idx+1}_score"}, inplace=True)

        # concat data
        pre_df = pre_df.merge(df, on="Username", how="outer")

    pre_df.set_index("Username", inplace=True)
    pre_df.sort_index(inplace=True)

    pre_df.fillna(0, inplace=True)
    
    # save csv
    pre_df.to_csv("result.csv")


if __name__ == "__main__":
    main()
