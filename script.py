import numpy as np
import pandas as pd

# iterate through all csv files and merge to one giant csv
data_list = []
for year in range(2000, 2014):
    # initialize data read
    data = pd.read_csv(str(year)[-2:] + str(year+1)[-2:] + '.csv')
    titles = data[data['N'].isnull()]['Student Characteristics']
    indices = pd.Series(index=titles, data=titles.index)

    # all disciplinary areas
    da_beg = indices['Disciplinary Area']
    da_end = titles.index[titles.index.get_loc(da_beg)+1] - 1
    da_overview = data.loc[da_beg+1:da_end]
    da_list = list(da_overview['Student Characteristics'])

    # all colleges
    college_beg = da_end + 1
    college_end = titles.index[titles.index.get_loc(college_beg)+1] - 1
    college_overview = data.loc[college_beg+1:college_end]
    college_list = list(college_overview['Student Characteristics'])

    # done with overall
    sep = data[data["Student Characteristics"] == "Total Population"].index[0]
    data = data.iloc[sep+1:]

    # select only interesting rows
    selector = data['Student Characteristics'] == 'College'
    for index in college_list:
        selector |= data['Student Characteristics'] == index

    # everything in one dataframe
    data = data[selector].rename(columns={'Student Characteristics': 'College'})
    data['Year'] = str(year) + '-' + str(year+1)
    data['Disciplinary Area'] = np.nan
    college_sep = data['College'] == 'College'
    college_index = data[college_sep].index

    # process each disciplinary area and label with college
    for i in range(len(da_list)-1):
        if i + 1 == len(college_index):
            sub = data.loc[college_index[i]+1:]
        else:
            sub = data.loc[college_index[i]+1:college_index[i+1]-1]
        sub.is_copy = False
        sub['Disciplinary Area'] = da_list[i]
        data_list.append(sub)

# commence output
giant_csv = pd.concat(data_list).set_index('Year')
print(giant_csv.head(20))
giant_csv.to_csv('total.csv', float_format=None)
