var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: __dirname+"/customer/js/index.js",
    output: {
        path: __dirname+"/customer/js/build",
        filename: "bundle.js"
    },
    plugins: [new HtmlWebpackPlugin({
        title: 'Html containing webpack Bundle',
        filename: __dirname + "/../templates/customer_bundle.html"
    })],
    module: {
        loaders: [
            {
                test: /.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['env', 'react']
                }
            }
        ]
    }
};