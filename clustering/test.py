def df_print_r_and_p_values(X, y):
    r_and_p_values = {col: stats.pearsonr(X[col], y) for col in X.columns}
    print("PEARSON'S R")


    for k, v in r_and_p_values.items():
        col = k
        r, p = v
        print(f"{col}:")
        print(f"\tPearson's R is {r:.2f} ")
        print(f"\twith a significance p-value of {p: .3}\n")

x_vars = ['bath','bed','finsqft', 'struct_tax_val',
          'land_tax_val']
df_print_r_and_p_values(sm_df[x_vars], log_df)
