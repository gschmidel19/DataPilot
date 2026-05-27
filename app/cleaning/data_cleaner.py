def remove_duplicates(df):

    original_rows = len(df)

    cleaned_df = df.drop_duplicates()

    removed_rows = original_rows - len(cleaned_df)

    return cleaned_df, removed_rows