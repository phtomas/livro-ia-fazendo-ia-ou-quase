-- Somente para a interface editável de revisão humana; não altera o Quarto final.
function Div(el)
  if el.classes:includes('na-pratica-com-ia') then
    el.attributes['custom-style'] = 'Bloco Pratica IA'
    return el
  end
  if el.classes:includes('experimento-do-leitor') then
    el.attributes['custom-style'] = 'Bloco Experimento'
    return el
  end
  if el.classes:includes('conceito-cartao') then
    el.attributes['custom-style'] = 'Cartao Conceito'
    return el
  end
  return nil
end
