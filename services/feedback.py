def get_clicked_titles(cursor):
    cursor.execute("SELECT title FROM clicks")
    return [row[0] for row in cursor.fetchall()]

def save_click(cursor, conn, title):
    cursor.execute("INSERT INTO clicks (title) VALUES (?)", (title,))
    conn.commit()

def get_feedback_scores(titles, clicked_titles):
    scores = []
    for t in titles:
        if t in clicked_titles:
            scores.append(0.3)
        else:
            scores.append(0)
    return scores