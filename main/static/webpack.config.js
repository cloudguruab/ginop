const HtmlWebpackPlugin = require("html-webpack-plugin"); //installed via npm
const path = require('path');

// FIXME: add webpack commands to package.json file
module.exports = {
  module: {
    entry: ['./src/index.js'],
    output: {
      path: path.resolve(__dirname, "dist"),
    },
    rules: [
      {
        test: /\.?js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  plugins: [new HtmlWebpackPlugin({ template: "../templates/src.html" })],
};
