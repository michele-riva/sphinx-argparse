"""Test the HTML builder and check output against XPath."""

import pytest

from .conftest import check_xpath


@pytest.mark.parametrize(
    "fname,expect_list",
    [
        (
            'index.html',
            [
                (".//h1", 'Sample'),
                (".//h1", 'blah-blah', False),
                (".//div[@class='highlight']//span", 'usage'),
                (".//h2", 'Positional Arguments'),
                (".//section[@id='positional-arguments']", ''),
                (".//section[@id='positional-arguments']/dl/dt[1]/kbd", 'foo2 metavar'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='bar-options']", ''),
                (".//section[@id='bar-options']/dl/dt[1]/kbd", '--bar'),
            ],
        ),
        (
            'subcommand-a.html',
            [
                (".//h1", 'Sample', False),
                (".//h1", 'Command A'),
                (".//div[@class='highlight']//span", 'usage'),
                (".//h2", 'Positional Arguments'),
                (".//section[@id='positional-arguments']", ''),
                (".//section[@id='positional-arguments']/dl/dt[1]/kbd", 'baz'),
            ],
        ),
        (
            'special-characters.html',
            [
                (".//h1", 'Sample', False),
                (".//h1", 'Special Characters'),
                (".//section/dl/dd/p", 'Default:'),
                (".//section/dl/dd/p/code/span", '420'),
                (".//section/dl/dd/p/code/span", "'*.rst"),
                (".//section/dl/dd/p/code/span", r"\['\*.rst',"),
            ],
        ),
        (
            'class-directive.html',
            [
                (".//h1", 'Sample', False),
                (".//h1", 'Argparse subclass'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//h1", 'Class returning parser, attribute'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[2]/kbd", '--attribute'),
                (".//h1", 'Class returning parser, instance method'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[2]/kbd", '--instance'),
                (".//h1", 'Class returning parser, class method'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[2]/kbd", '--class'),
                (".//h1", 'Class returning parser, static method'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[2]/kbd", '--static'),
                (".//h1", 'Class returning parser, property'),
                (".//div[@class='highlight']//pre", 'usage'),
                (".//h2", 'Named Arguments'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[1]/kbd", '--foo'),
                (".//section[@id='named-arguments']", ''),
                (".//section[@id='named-arguments']/dl/dt[2]/kbd", '--property'),
            ],
        ),
    ],
)
@pytest.mark.sphinx('html', testroot='default-html')
def test_default_html(app, cached_etree_parse, fname, expect_list):
    app.build()
    print(app.outdir / fname)
    for expect in expect_list:
        check_xpath(cached_etree_parse(app.outdir / fname), fname, *expect)
