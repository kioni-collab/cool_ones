import psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import RealDictCursor
from util import safe_int, safe_sort_by, safe_sort_dir
from sets import count_sets, search_sets
import math
conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)

app = Flask(__name__)

# TODO: create /sets HTML endpoint

@app.route("/sets")
def search_sets_html():
    set_name = request.args.get('set_name', '')
    theme_name = request.args.get('theme_name', '')
    page = safe_int(request.args.get('page'), 1)
    limit = safe_int(request.args.get('results_per_page'),50)
    offset =  (page -1) * limit
    sort_by = safe_sort_by(request.args.get('sort_by'), 'set_name')
    sort_dir  = safe_sort_dir(request.args.get('sort_dir'), 'asc')
    part_count_gte = safe_int(request.args.get('part_count_gte'), 0)
    part_count_lte = safe_int(request.args.get('part_count_lte'), 999999)
    




    # TODO: all the other params
    with conn.cursor() as cur:
        count = count_sets(cur, set_name_contains=set_name,
                           theme_name_contains=theme_name, part_count_gte=part_count_gte, part_count_lte=part_count_lte)
        results = search_sets(cur, set_name_contains=set_name, theme_name_contains= theme_name, part_count_gte=part_count_gte, part_count_lte=part_count_lte,
                              limit=limit, offset=offset, sort_by= sort_by, sort_dir=sort_dir)
        page_count  = int(math.ceil(count/limit))
        return render_template('sets.html', count=count, results=results, set_name=set_name, theme_name = theme_name,
        page=page, limit=limit, sort_by = sort_by, sort_dir=sort_dir, part_count_gte = part_count_gte, 
        part_count_lte = part_count_lte, page_count = page_count)
