import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

class Home extends Component {
  render() {
    const { posts } = this.props;
    const postList = posts.length ? (
      posts.map((post) => {
        return (
          <div className="post card" key={post.id}>
            <img src="blog.png" alt="Post" />
            <Link to={"/post/" + post.id}>
              <span className="card-title">{post.title}</span>
            </Link>
          </div>
        );
      })
    ) : (
      <p>No post to show</p>
    );

    return <div className="container home">{postList}</div>;
  }
}

const mapStateToProps = (state) => {
  return {
    posts: state.posts,
  };
};

export default connect(mapStateToProps)(Home);
