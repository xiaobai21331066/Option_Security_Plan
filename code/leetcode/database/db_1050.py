import pandas as pd


mysql_method = """select actor_id, director_id from ActorDirector group by actor_id, director_id
having count(actor_id) >= 3"""

def pd_method(df):
    tmp_df = df.groupby(['actor_id','director_id']).count()
    tmp_df.rename(columns={'timestamp':'total'}, inplace=True)
    tmp_df.reset_index(inplace=True)
    tmp_df = tmp_df[['actor_id','director_id']][tmp_df['total'] >= 3]
    # print('tmp_df', tmp_df)
    return tmp_df
