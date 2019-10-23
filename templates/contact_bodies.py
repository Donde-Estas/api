initial_contact_body = """
<h3>Hola {contact_name}!</h3>
<p>
    Si te ha llegado este mail, es porque ingresaste a {missing_name}
    en la página ¿Dónde Están? por sospecha de desaparición.
    En caso de que creas que esto fue un error,
    se agradecería responder este mail con el asunto ERROR.
    En caso contrario, y si llegas a conocer el paradero de
    {missing_name}, por favor haz click en el siguiente botón
    para actualizar su estado en la página:
</p>
{find_person_button}
<p>
    La clave para acceder a la página y marcar a {contact_name} como
    encontrad@ es: <strong>{key}</strong>
</p>
""".replace("\n", " ").replace("  ", " ")
