const initialState = {
    posts: [
      {
        id: "1",
        title: "Sunt aut facere repellat provident occaecati...",
        body:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit...",
      },
      {
        id: "2",
        title: "Dolorem eum magni eos aperiam quia",
        body:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit...",
      },
      {
        id: "3",
        title: "Ea molestias quasi exercitationem repellat qui ipsa...",
        body:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit...",
      },
    ],
  };
  
  const rootReducer = (state = initialState, action) => {
    if (action.type === "DELETE_POST") {
      const newPosts = state.posts.filter((post) => post.id !== action.id);
      return {
        ...state,
        posts: newPosts,
      };
    }
    return state;
  };
  
  export default rootReducer;
  