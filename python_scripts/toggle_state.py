# ------------------------------------------------------------------------
# Toggle numberic state of the entity specified in the automation's action
# ------------------------------------------------------------------------

entity_id = data.get('entity_id')

if entity_id is not None:
    logger.warning("Entity {}".format(entity_id))
    obj = hass.states.get(entity_id)
    state = int(obj.state)
    attributes = obj.attributes.copy()

    logger.warning("Old state {}".format(state))

    state = !state

    logger.warning("New state {}".format(state))

    hass.states.set(entity_id, state, attributes)
