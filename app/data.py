# Define a function to manipulate data with pandas
def legislators_support_oppose(legislators, vote_result):

    merged_data = legislators.merge(vote_result, left_on='id', right_on='legislator_id')
    grouped_data = merged_data.groupby(['legislator_id', 'name', 'vote_type']).size().reset_index(name='vote_count')
    grouped_data.rename(columns={'legislator_id': 'id'}, inplace=True)

    supported_bills = grouped_data[grouped_data['vote_type'] == 1].rename(columns={'vote_count': 'num_supported_bills'}).drop(columns=['vote_type'])
    opposed_bills = grouped_data[grouped_data['vote_type'] == 2].rename(columns={'vote_count': 'num_opposed_bills'}).drop(columns=['vote_type'])

    legislators_result = supported_bills.merge(opposed_bills, on=['id', 'name'])

    return legislators_result

# Define a function to manipulate data with pandas
def bills_support_oppose(bills, legislators, vote_result, votes):

    merged_data = votes.merge(bills, left_on='bill_id', right_on='id').rename(columns={'id_x': 'id'}).merge(vote_result, left_on='id', right_on='vote_id').merge(legislators, left_on='sponsor_id', right_on='id' , how='left')
    merged_data = merged_data.fillna('Unknown')

    grouped_data = merged_data.groupby(['bill_id', 'title', 'vote_type', 'name']).size().reset_index(name='vote_count')

    grouped_data.rename(columns={'bill_id': 'id', 'name': 'primary_sponsor'}, inplace=True)

    supported_bills = grouped_data[grouped_data['vote_type'] == 1].rename(columns={'vote_count': 'supporter_count'}).drop(columns=['vote_type'])
    opposed_bills = grouped_data[grouped_data['vote_type'] == 2].rename(columns={'vote_count': 'opposer_count'}).drop(columns=['vote_type'])

    bills_result = supported_bills.merge(opposed_bills, on=['id', 'title', 'primary_sponsor'])

    return bills_result