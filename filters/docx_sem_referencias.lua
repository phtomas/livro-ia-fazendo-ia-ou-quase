-- A bibliografia permanece na fonte canônica e é revisada no bloco Anexos;
-- evita sua repetição e páginas órfãs nos blocos DOCX intermediários.
function Div(el)
  if el.identifier=='refs' then return {} end
  return nil
end
