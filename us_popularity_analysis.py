# us_popularity_analysis.py
from imports import *

def run_us_popularity_analysis(df):

    st.subheader("US Popularity Analysis")

    # Sort top 10 states
    df = df.sort_values(by='total_tweet_count', ascending=False)
    # The top 10 states based on total tweet counts
    top_states = df.iloc[1:].head(10)
    # Set the position of bars on the x-axis
    bar_width = 0.25
    x = range(len(top_states))
    # Create a figure for the bar chart
    plt.figure(figsize=(12, 6))
    # Plot Trump tweets
    plt.bar(x, top_states['trump_count'], width=bar_width, label='Trump Tweets', color='red', align='center')
    # Plot Biden tweets
    plt.bar([p + bar_width for p in x], top_states['biden_count'], width=bar_width, label='Biden Tweets', color='blue', align='center')
    # Plot Total tweets
    plt.bar([p + bar_width*2 for p in x], top_states['total_tweet_count'], width=bar_width, label='Total Tweets', color='gray', align='center')
    # Adding labels and title
    plt.xlabel('State', fontsize=14, color='white')
    plt.ylabel('Tweet Count', fontsize=14, color='white')
    # plt.title('Top 10 States Tweet Counts: Trump vs Biden vs Total', fontsize=16, color='white', weight='bold')
    plt.xticks([p + bar_width for p in x], top_states['state'], rotation=90, color='white')
    plt.legend(facecolor='white', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)  # Add gridlines
    # Change tick values to white
    plt.tick_params(axis='x', colors='white')  # X-axis ticks
    plt.tick_params(axis='y', colors='white')  # Y-axis ticks
    # Streamlit display
    st.pyplot(plt, transparent=True)
    # Clear the figure after displaying
    plt.clf()

    unique_states = sorted(list(set(df['state'].unique())))
    selected_state = st.selectbox('Select state', unique_states)

    # Calculate percentage for selected state
    trump_percentage = df.loc[df['state'] == selected_state, 'trump_percentage'].values[0]
    biden_percentage = df.loc[df['state'] == selected_state, 'biden_percentage'].values[0]
    # Calculate US percentage
    # trump_percentage_US = df.loc[df['state'] == 'US', 'trump_percentage'].values[0]
    # biden_percentage_US = df.loc[df['state'] == 'US', 'biden_percentage'].values[0]

    # Calculate state_tweet_count / US_tweet_count
    state_US_percentage = df.loc[df['state'] == selected_state, 'total_percentage'].values[0]

    ### Row A
    st.markdown(f'### {selected_state}')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Trump", f'{trump_percentage}%')

    with col2:
        st.metric("Biden", f'{biden_percentage}%')

    with col3:
        st.metric("state/World", f'{state_US_percentage}%')
   
    ### Row B
    st.markdown('### Map')

    map_data = df.sort_values(by='state', ascending=True)
    map_data['difference'] = df['trump_count'] - df['biden_count'] 

    # Normalize the difference for color mapping
    map_data['color'] = map_data['difference'].apply(lambda x: max(min(x, 100), -100))  # Cap between -100 and 100

    # Create a choropleth map
    fig = px.choropleth(
        map_data,
        locationmode='USA-states',
        locations='state_code',
        color='color',
        color_continuous_scale=[(1, 'red'), (0, 'blue')],
        range_color=[-100, 100],  # Adjust this range based on your data
        scope="usa",
        # title='Biden vs Trump Tweet Percentages by State',
        hover_name='state',  # Show the state code on hover
        hover_data={
            'trump_percentage': True,  # Display Trump percentage
            'biden_percentage': True,   # Display Biden percentage
            'color': False              # Do not display the difference
        }
    )
    # Update layout for better visualization with a transparent background
    fig.update_layout(
        # title_font=dict(size=16, color='white'),
        paper_bgcolor='rgba(255, 255, 255, 0)',  # Set paper background color to transparent
        geo=dict(bgcolor='rgba(255, 255, 255, 0)'),  # Set geo background color to transparent
        coloraxis_showscale=False,  # Hide the color scale (legend)
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    ### Row C
    most_us_df = load_data("most_us_df.csv")
    # Add a selectbox for selecting either "Trump" or "Biden"
    selected_candidate = st.selectbox('Select Candidate', ['Trump', 'Biden'])

    # Dynamically filter the DataFrame based on the selected candidate
    if selected_candidate == 'Trump':
        filtered_df = most_us_df[most_us_df['candidate'] == 'Trump']
    else:
        filtered_df = most_us_df[most_us_df['candidate'] == 'Biden']

    # Display the Top 5 Most Liked Tweets
    st.markdown('### Top 5 Most Liked Tweets')
    # Top 10 most liked tweets for the selected state
    top_liked_tweets = filtered_df[filtered_df['state'] == selected_state].nlargest(5, 'likes')
    # Display the dataframe without index and extend it to fill the page
    st.dataframe(
        top_liked_tweets[['tweet', 'likes']],  # Display only the 'tweet' and 'likes' columns
        hide_index=True,  # Hide the index numbers
        use_container_width=True  # Extend the table to fill the page width
    )

    # Display the Top 5 Most Retweeted Tweets
    st.markdown('### Top 5 Most Retweeted Tweets')
    # Select top 5 most retweeted tweets for the selected state
    top_retweeted_tweets = filtered_df[filtered_df['state'] == selected_state].nlargest(5, 'retweet_count')

    # Display the dataframe
    st.dataframe(
        top_retweeted_tweets[['tweet', 'retweet_count']],  # Display 'tweet' and 'retweet_count' columns
        hide_index=True,  # Hide index numbers
        use_container_width=True  # Extend the table to fill the page width
    )
