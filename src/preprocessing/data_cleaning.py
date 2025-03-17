import pandas as pd



def preprocessing(csv) :

    df = pd.read_csv(csv)

    df_no_date = df.drop(["Fecha", "ClasDef"], axis=1)
    df_no_date["RatOf"] = df_no_date["RatOf"].apply(lambda x: x.replace(",", ""))
    df_no_date["RatOf"] = df_no_date["RatOf"].astype(float)

    df_no_date["Sec_played"] = df_no_date["Min"].apply(lambda x: (int(x[:2]) * 60) + int(x[-2:]))
    df_no_date = df_no_date.drop("Min", axis=1)

    df_dummies = pd.get_dummies(df["Equipo"], drop_first=True)
    df_encoded = pd.concat([df_no_date, df_dummies], axis=1).drop("Equipo", axis=1)
    
    df_encoded.to_csv("data/processed/preprocessed_data.csv")
    print("File uploaded succesfully")