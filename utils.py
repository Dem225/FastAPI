vscode_lsp_terminal_prompt_tracker= {}
from herores import HEROES


def find_proprehero_id(hero):
    # hero["id"] = 1 if len(HEROES) ==0  else HEROES[-1].get("id") +1

    
    if len(HEROES)==0:
        hero["id"] ==1
    else:
        hero.id = HEROES[-1].id + 1


    return hero