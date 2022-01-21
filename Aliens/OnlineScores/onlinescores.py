import pygsheets


def get_highscores():
    google_sheet = pygsheets.authorize(service_file='Data/service_account_credentials.json')
    work_sheet = google_sheet.open_by_url("https://docs.google.com/spreadsheets/d/1rkKbKDpU3oK8NKunMbhkNNrIUarewOvOGU4zccAvwtQ/edit?usp=sharing")
    return work_sheet[0].get_all_records(empty_value='', head=1, majdim='ROWS', numericise_data=True)



def get_smallest_value():
    try:
        google_sheet = pygsheets.authorize(service_file='Data/service_account_credentials.json')
        work_sheet = google_sheet.open_by_url("https://docs.google.com/spreadsheets/d/1rkKbKDpU3oK8NKunMbhkNNrIUarewOvOGU4zccAvwtQ/edit?usp=sharing")
        scores = work_sheet[0].get_all_records(empty_value='', head=1, majdim='ROWS', numericise_data=True)

        if len(scores) < 10:
            return 0
        else:
            return scores[-1]['Score']

    except Exception:
        return {}


def update_highscores(score, name):
    google_sheet = pygsheets.authorize(service_file='Data/service_account_credentials.json')
    work_sheet = google_sheet.open_by_url("https://docs.google.com/spreadsheets/d/1rkKbKDpU3oK8NKunMbhkNNrIUarewOvOGU4zccAvwtQ/edit?usp=sharing")
    high_scores = work_sheet[0].get_all_records(empty_value='', head=1, majdim='ROWS', numericise_data=True)
    high_scores_len = len(high_scores)

    for place, high_score in enumerate(high_scores):
        if score > high_score['Score']:
            work_sheet[0].insert_rows(place + 1, 1, [name, score])
            high_scores_len += 1
            work_sheet[0].delete_rows(12, high_scores_len - 10)
            return None

    if high_scores_len < 10:
        work_sheet[0].insert_rows(len(high_scores) + 1, 1, [name, score])


