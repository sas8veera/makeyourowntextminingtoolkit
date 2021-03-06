# module with visualisation functions

import os
import wordcloud
import matplotlib.pyplot as plt

import numpy

import IPython.core.display
import networkx
import networkx.readwrite.json_graph
import random

# word cloud from pandas frame of word and freq
def plot_wordcloud(word_count):
    # wordcloud object
    wc = wordcloud.WordCloud(max_words=100, width=1200, height=800, background_color="white", margin=10,
                             prefer_horizontal=1.0)

    # words and plot sizes (word count, relevance, etc)
    wc.generate_from_frequencies(word_count.to_dict()[word_count.columns[0]])

    # plot wordcloud
    plt.figure(dpi=600, figsize=(6,4))
    plt.imshow(wc)
    plt.axis("off")
    pass


# force-directed graph
def plot_force_directed_graph(node1_node1_weight):
    # column names for node source and target, and edge attributes
    node_source_name = node1_node1_weight.columns.values[0]
    node_target_name = node1_node1_weight.columns.values[1]
    link_edge_name = node1_node1_weight.columns.values[2]

    # convert node1_node1_weight to graph
    graph = networkx.from_pandas_dataframe(node1_node1_weight, source=node_source_name, target=node_target_name, edge_attr=link_edge_name)

    # convert graph nodes and inks to json, ready for d3
    graph_json = networkx.readwrite.json_graph.node_link_data(graph)
    graph_json_nodes = graph_json['nodes']
    graph_json_links = graph_json['links']
    #print(str(graph_json_nodes))
    #print(str(graph_json_links))

    # read html template
    html_template_file = os.path.join(os.path.dirname(__file__), 'html_templates/d3_force_directed_graph.html')
    with open(html_template_file, mode='r') as f:
        html = f.read()
        pass

    # read javascript template
    js_template_file = os.path.join(os.path.dirname(__file__), 'html_templates/d3_force_directed_graph.js')
    with open(js_template_file, mode='r') as f:
        js = f.read()
        pass

    # generate random identifier for SVG element, to avoid name clashes if used multiple times in a notebook
    random_id_string = str(random.randrange(1000000,9999999))
    # replace placeholder in both html and js templates
    html = html.replace('%%unique-id%%', random_id_string)
    js = js.replace('%%unique-id%%', random_id_string)

    # substitute links and data
    js = js.replace('%%links%%', str(graph_json_links))
    js = js.replace('%%nodes%%', str(graph_json_nodes))
    js = js.replace('%%edge_attribute%%', link_edge_name)
    #print(html)
    #print(js)

    # display html in notebook cell
    IPython.core.display.display_html(IPython.core.display.HTML(html))
    # display (run) javascript in notebook cell
    IPython.core.display.display_javascript(IPython.core.display.Javascript(data=js))
    pass


# force-directed graph2
def plot_force_directed_graph2(node1_node1_weight):
    # column names for node source and target, and edge attributes
    node_source_name = node1_node1_weight.columns.values[0]
    node_target_name = node1_node1_weight.columns.values[1]
    link_edge_name = node1_node1_weight.columns.values[2]

    # convert node1_node1_weight to graph
    graph = networkx.from_pandas_dataframe(node1_node1_weight, source=node_source_name, target=node_target_name, edge_attr=link_edge_name)

    # convert graph nodes and inks to json, ready for d3
    graph_json = networkx.readwrite.json_graph.node_link_data(graph)
    graph_json_nodes = graph_json['nodes']
    graph_json_links = graph_json['links']
    #print(str(graph_json_nodes))
    #print(str(graph_json_links))

    # read html template
    html_template_file = os.path.join(os.path.dirname(__file__), 'html_templates/d3_force_directed_graph.html')
    with open(html_template_file, mode='r') as f:
        html = f.read()
        pass

    # read javascript template
    js_template_file = os.path.join(os.path.dirname(__file__), 'html_templates/d3_force_directed_graph.js')
    with open(js_template_file, mode='r') as f:
        js = f.read()
        pass

    # generate random identifier for SVG element, to avoid name clashes if used multiple times in a notebook
    random_id_string = str(random.randrange(1000000,9999999))
    # replace placeholder in both html and js templates
    html = html.replace('%%unique-id%%', random_id_string)
    js = js.replace('%%unique-id%%', random_id_string)

    # substitute links and data
    js = js.replace('%%links%%', str(graph_json_links))
    js = js.replace('%%nodes%%', str(graph_json_nodes))
    js = js.replace('%%edge_attribute%%', link_edge_name)
    #print(html)
    #print(js)

    # display html in notebook cell
    IPython.core.display.display_html(IPython.core.display.HTML(html))
    # display (run) javascript in notebook cell
    IPython.core.display.display_javascript(IPython.core.display.Javascript(data=js))
    pass

# bar chart
def plot_bar_chart(data_series):
    plt.bar(numpy.arange(len(data_series)), data_series.values)
    pass


# scatter 2-d plot
def plot_scatter_chart(xy_data):

    # plot as scatter plot
    p = plt.subplot(111)
    p.axis('scaled');
    #p.axis([-2, 2, -2, 2]);
    p.axhline(y=0, color='lightgrey');
    p.axvline(x=0, color='lightgrey')
    p.set_yticklabels([]);
    p.set_xticklabels([])

    p.set_title("S_reduced_VT")
    p.plot(xy_data.iloc[0], xy_data.iloc[1], 'ro')

    plt.show()
    pass