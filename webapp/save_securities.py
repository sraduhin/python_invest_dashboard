from webapp.model import db, Securities

def save_securities(figi, instrument_type, currency, quantity, average_position_price,
                    expected_yield, current_nkd, average_position_price_pt, current_price,
                    average_position_price_fifo, quantity_lots):
    position_securities = Securities(figi=figi, instrument_type=instrument_type,
                                    currency=currency, quantity=quantity,
                                    average_position_price=average_position_price,
                                    expected_yield=expected_yield, current_nkd=current_nkd,
                                    average_position_price_pt=average_position_price_pt,
                                    current_price=current_price,
                                    average_position_price_fifo=average_position_price_fifo,
                                    quantity_lots=quantity_lots)
    db.session.add(position_securities)
    db.session.commit()