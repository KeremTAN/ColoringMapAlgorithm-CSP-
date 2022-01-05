import plotly.express as px

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

colors = ["blue", "green", "red", "yellow"]

graphOfCountries = {"Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
                    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
                    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay",
                               "Venezuela"],
                    "Chile": ["Argentina", "Bolivia", "Peru"],
                    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
                    "Ecuador": ["Colombia", "Bolivia", "Peru"],
                    "Falkland Islands": [],
                    "Guyana": ["Brazil", "Suriname", "Venezuela"],
                    "Paraguay": ["Argentina", "Bolivia", "Brazil"],
                    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
                    "Suriname": ["Brazil", "Guyana"],
                    "Uruguay": ["Argentina", "Brazil"],
                    "Venezuela": ["Brazil", "Colombia", "Guyana"]
                    }


def sortCountries(graph, unSortedCountries):
    newCountry = {}
    retCountries = []
    for country in unSortedCountries:
        newCountry.update({country: len(graph[country])})

    newCountry = list(sorted(newCountry.items(), key=lambda kv: kv[1]))

    i = len(newCountry) - 1
    while i > -1:
        retCountries.append(newCountry[i][0])
        i -= 1

    return retCountries


# Is the condition satisfied?
def isColoredTheTrue(graph, testMap):
    for node in graph:
        edges = (graph[node])
        if node in testMap.keys():
            colorOfNode = testMap[node]
            for edge in edges:
                if edge in testMap.keys():
                    colorOfEdge = testMap[edge]
                    if colorOfNode == colorOfEdge:
                        return False
    return True


def colorTheCountry(graph, colorMap, unSortedCountries):
    sortedCountries = sortCountries(graphOfCountries, unSortedCountries)
    clr_ix = 1
    cntry_ix = 0
    solverCounter = 0
    isSolved = True
    while cntry_ix < len(sortedCountries):
        if solverCounter == len(colors):
            print("Unsolved Problem")
            isSolved = False
            break
        tmpIx = cntry_ix
        colorMap.update({sortedCountries[cntry_ix]: colors[clr_ix]})
        if not isColoredTheTrue(graph, colorMap):
            cntry_ix -= 1
        if clr_ix < 3:
            clr_ix += 1
        else:
            clr_ix = 0
        cntry_ix += 1
        if tmpIx == cntry_ix:
            solverCounter += 1
        else:
            solverCounter = 0
    return colorMap, isSolved


# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


if __name__ == "__main__":
    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    print(f"colormap_test {isColoredTheTrue(graphOfCountries, colormap_test)} colored.")
    coloringMap = {}
    coloringMap, isTrue = colorTheCountry(graphOfCountries, coloringMap, countries)
    print(f"coloringMap {isColoredTheTrue(graphOfCountries, coloringMap)} colored.")
    if isTrue:
        plot_choropleth(colormap=coloringMap)
